from __future__ import annotations

import enum
import types
import typing
from typing import Callable, Coroutine, Any
import inspect

from pydantic import validate_arguments


from DiscordInterpythons.models.interaction import Interaction, InteractionResponse
from DiscordInterpythons.models.model_type import (
    InteractionType,
    ApplicationCommandOptionType,
    ComponentType,
    ApplicationCommandType,
    ButtonStyleType,
)
from DiscordInterpythons.models.application_command import (
    ApplicationCommand,
    ApplicationCommandOption,
    ApplicationCommandOptionChoice,
)
from DiscordInterpythons.models.interaction_data import InteractionDataOption
from DiscordInterpythons.models.emoji import PartialEmoji
from DiscordInterpythons.models.component import Button
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.channel import PartialChannel
from DiscordInterpythons.models.role import Role
from DiscordInterpythons.models.attachment import Attachment


__all__ = (
    "InteractionHandlerClass",
    "ChatInputHandler",
    "SubCommandHandler",
    "AutoCompleteHandler",
    "ButtonHandler",
)


class _InteractionHandlerMetaClass(type):
    _cls_storage: dict[typing.Type[InteractionHandlerClass], list[_Handler, ...]] = {}
    _handlers: list[_Handler]
    _chat_input_handler_storage: dict[str, ChatInputHandler] = {}
    _button_handler_store: dict[str, ButtonHandler] = {}

    def __new__(mcs, name, bases, attrs, **kwargs):
        cls = super().__new__(mcs, name, bases, attrs)

        if name == "InteractionHandlerClass":
            return cls

        assert issubclass(cls, InteractionHandlerClass)

        mcs._cls_storage[cls] = []
        for name, method in attrs.items():
            if isinstance(method, _Handler):
                mcs._cls_storage[cls].append(method)

            if isinstance(method, ChatInputHandler) and not isinstance(method, SubCommandHandler):
                mcs._chat_input_handler_storage[method.name] = method

            if isinstance(method, ButtonHandler):
                mcs._button_handler_store[method.custom_id] = method
        return cls

    @classmethod
    def register_handler(mcs, inst: InteractionHandlerClass):
        for chat_input in mcs._cls_storage[type(inst)]:
            chat_input._parent_self = inst

    @classmethod
    async def call(mcs, interaction: Interaction) -> InteractionResponse:
        if interaction.type in (
                InteractionType.APPLICATION_COMMAND,
                InteractionType.APPLICATION_COMMAND_AUTOCOMPLETE,
        ):
            handler = mcs._chat_input_handler_storage.get(interaction.data.name)

            assert handler

            return await handler._call(interaction)
        elif interaction.type == InteractionType.MESSAGE_COMPONENT \
                and interaction.data.component_type == ComponentType.BUTTON:
            handler_id = interaction.data.custom_id.split(":")

            handler = mcs._button_handler_store.get(handler_id[0])

            assert handler

            return await handler._call(interaction, "".join(handler_id[1:]))

        assert True is False

    @classmethod
    def generate_application_commands(mcs) -> ApplicationCommand.S:
        application_commands: list[ApplicationCommand] = []

        for key, value in mcs._chat_input_handler_storage.items():
            application_commands.append(value._generate_application_command())

        return tuple(application_commands)


class InteractionHandlerClass(metaclass=_InteractionHandlerMetaClass):
    def __init__(self):
        _InteractionHandlerMetaClass.register_handler(self)


class _Handler:
    _parent_self: None | InteractionHandlerClass = None


class ChatInputHandler(_Handler):
    _sub_commands: dict[str, ChatInputHandler]
    _auto_completes: dict[str, AutoCompleteHandler]

    def __init__(
            self,
            name: None | str = None,
            auto_completes: None | dict[str, AutoCompleteHandler] = None,
    ):
        self.application_command: None | _application_command_handler = None
        self._name = name
        self._sub_commands = {}
        self._auto_completes = auto_completes or {}

    def __call__(self, application_command: _application_command_handler):
        self.application_command = validate_arguments(application_command)

        return self

    @property
    def name(self) -> str:
        return self._name or self.application_command.__name__

    async def _call(
            self,
            interaction: Interaction,
            data_option: None | InteractionDataOption = None,
    ) -> InteractionResponse:
        assert interaction.data is not None

        options: dict[str, Any] = {}
        iterative_options = data_option.options if data_option is not None else interaction.data.options

        for option in iterative_options or ():
            if option.focused:
                return await self._auto_completes[option.name]._call(interaction, iterative_options, option.value)
            elif (
                    option.type == ApplicationCommandOptionType.SUB_COMMAND_GROUP
                    or option.type == ApplicationCommandOptionType.SUB_COMMAND
            ):
                return await self._sub_commands[option.name]._call(interaction, option)
            elif option.type == ApplicationCommandOptionType.USER:
                options[option.name] = interaction.data.resolved.roles[option.value]
            elif option.type == ApplicationCommandOptionType.CHANNEL:
                options[option.name] = interaction.data.resolved.channels[option.value]
            elif option.type == ApplicationCommandOptionType.ROLE:
                options[option.name] = interaction.data.resolved.roles[option.value]
            elif option.type == ApplicationCommandOptionType.ATTACHMENT:
                options[option.name] = interaction.data.resolved.attachments[option.value]
            else:
                options[option.name] = option.value

        return await self.application_command(self._parent_self, interaction, **options)

    def _generate_application_command_options(self) -> tuple[ApplicationCommandOption, ...]:
        description, param_descriptions = _doc_parser(self.application_command.__doc__)

        func_annotations = inspect.get_annotations(self.application_command, eval_str=True)

        if "self" in func_annotations:
            func_annotations.pop("self")
        if "interaction" in func_annotations:
            func_annotations.pop("interaction")
        if "return" in func_annotations:
            func_annotations.pop("return")

        options = []
        for param, annotation in func_annotations.items():
            required = True

            if typing.get_origin(annotation) is types.UnionType:
                union_items = typing.get_args(annotation)
                assert len(union_items) == 2
                assert union_items[0] is types.NoneType
                annotation = union_items[1]
                required = False

            choices = None

            if issubclass(annotation, str) and issubclass(annotation, enum.Enum):
                choices = list(zip(annotation._member_names_, annotation._value2member_map_.keys()))
                annotation = str

            elif issubclass(annotation, enum.Enum):
                choices = list(zip(annotation._member_names_, annotation._value2member_map_.keys()))
                annotation = int

            try:
                option_type = _application_command_option_map[annotation]
            except KeyError:
                print(f"Error with {param} and {annotation}")
                continue

            try:
                param_description = param_descriptions[param]
            except KeyError:
                print(f"No doc for {param}")
                param_description = ""

            options.append(ApplicationCommandOption(
                type=option_type,
                name=param,
                description=param_description,
                choices=tuple(ApplicationCommandOptionChoice(name=name, value=value) for name, value in choices) if choices is not None else None,
                required=required,
                autocomplete=(
                    param in self._auto_completes
                    and option_type == ApplicationCommandOptionType.STRING
                ) or None
            ))

        for key, value in self._sub_commands.items():
            options.append(ApplicationCommandOption(
                type=ApplicationCommandOptionType.SUB_COMMAND
                if len(value._sub_commands) == 0 else ApplicationCommandOptionType.SUB_COMMAND_GROUP,
                name=key,
                description=value.description[0],
                options=value._generate_application_command_options(),
            ))

        return tuple(options)

    def _generate_application_command(self) -> ApplicationCommand:
        return ApplicationCommand(
            type=ApplicationCommandType.CHAT_INPUT,
            name=self.name,
            description=self.description[0],
            options=self._generate_application_command_options(),
        )

    def sub_command(
            self,
            name: None | str = None,
            auto_completes: None | dict[str, AutoCompleteHandler] = None,
    ) -> ChatInputHandler:
        return SubCommandHandler(
            name=name,
            sub_command_parent=self,
            auto_completes=auto_completes,
        )

    @property
    def description(self) -> tuple[str, dict[str, str]]:
        return _doc_parser(self.application_command.__doc__)


class SubCommandHandler(ChatInputHandler):
    sub_command_parent: None | ChatInputHandler = None

    def __init__(
            self,
            name: None | str = None,
            sub_command_parent: ChatInputHandler = None,
            auto_completes: None | dict[str, AutoCompleteHandler] = None
    ):
        self.sub_command_parent = sub_command_parent
        super().__init__(name=name, auto_completes=auto_completes)

    def __call__(self, application_command: _application_command_handler):
        if self.sub_command_parent:
            self.sub_command_parent._sub_commands[self.name] = self

        return super().__call__(application_command)

    def sub_command(
            self,
            name: None | str = None,
            auto_completes: None | dict[str, AutoCompleteHandler] = None,
    ) -> SubCommandHandler:
        return SubCommandHandler(
            name=name,
            sub_command_parent=self,
            auto_completes=auto_completes,
        )


class AutoCompleteHandler(_Handler):
    handler: None | _auto_complete_handler = None

    def __call__(self, handler: _auto_complete_handler):
        self.handler = validate_arguments(handler)

        return self

    async def _call(
            self,
            interaction: Interaction,
            options: InteractionDataOption.S,
            value: str,
    ) -> InteractionResponse:
        return await self.handler(self._parent_self, interaction, {i.name: i for i in options}, value)


class ButtonHandler(_Handler):
    handler: None | _button_handler = None

    def __init__(self, custom_id: str):
        self.custom_id = custom_id

    def __call__(self, handler: _button_handler):
        self.handler = validate_arguments(handler)

        return self

    async def _call(
            self,
            interaction: Interaction,
            custom_id: str,
    ) -> InteractionResponse:
        return await self.handler(self._parent_self, interaction, custom_id)

    def build(
            self,
            custom_id: str,
            label: str,
            emoji: PartialEmoji = None,
            style: ButtonStyleType = ButtonStyleType.Primary,
            url: str = None,
            disabled: bool = False,
    ) -> Button:
        return Button(
            type=ComponentType.BUTTON,
            style=style,
            label=label,
            emoji=emoji,
            custom_id=f"{self.custom_id}:{custom_id}",
            url=url,
            disabled=disabled,
        )


_auto_complete_handler = Callable[
    [InteractionHandlerClass, Interaction, dict[str, InteractionDataOption], str],
    Coroutine[Any, Any, None | InteractionResponse]
]


_button_handler = Callable[
    [InteractionHandlerClass, Interaction, str],
    Coroutine[Any, Any, None | InteractionResponse]
]


_application_command_handler = Callable[
    [InteractionHandlerClass, Interaction, tuple[Any, ...], dict[str, Any]],
    Coroutine[Any, Any, None | InteractionResponse]
]

_application_command_option_map = {
    str: ApplicationCommandOptionType.STRING,
    int: ApplicationCommandOptionType.INTEGER,
    bool: ApplicationCommandOptionType.BOOLEAN,
    User: ApplicationCommandOptionType.USER,
    PartialChannel: ApplicationCommandOptionType.CHANNEL,
    Role: ApplicationCommandOptionType.ROLE,
    float: ApplicationCommandOptionType.NUMBER,
    Attachment: ApplicationCommandOptionType.ATTACHMENT,
}


def _doc_parser(doc_string: None | str) -> tuple[str, dict[str, str]]:
    if doc_string is None:
        return "", {}

    res = doc_string.split("\n\n")
    res = [i.strip() for i in res]

    short_description = res[0]

    res = res[-1].split("\n")
    res = [i.strip() for i in res]
    params = {}

    for i in res:
        if ":param" in i:
            key, value = i[1:].split(": ")
            params[key.split(" ")[-1]] = value

    return short_description, params
