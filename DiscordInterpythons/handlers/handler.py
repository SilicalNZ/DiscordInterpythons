from __future__ import annotations

import enum
import types
import typing
from typing import Callable, Coroutine, Any
import inspect

from pydantic import validate_arguments

from DiscordInterpythons import models


class _InteractionHandlerMetaClass(type):
    _cls_storage: dict[typing.Type[InteractionHandlerClass], list[ChatInputHandler, ...]] = {}
    _command_storage: dict[str, ChatInputHandler] = {}

    def __new__(mcs, name, bases, attrs, **kwargs):
        cls = super().__new__(mcs, name, bases, attrs)

        if name == "InteractionHandlerClass":
            return cls

        mcs._cls_storage[cls] = []
        for name, method in attrs.items():
            if isinstance(method, ChatInputHandler):
                mcs._command_storage[method.name] = method
                mcs._cls_storage[cls].append(method)

        return cls

    @classmethod
    def register_handler(mcs, inst: InteractionHandlerClass):
        for chat_input in mcs._cls_storage[type(inst)]:
            chat_input.parent_self = inst

    @classmethod
    async def call(mcs, interaction: models.Interaction) -> models.InteractionResponse:
        handler = mcs._command_storage.get(interaction.data.name)

        assert handler

        return await handler._call(interaction)

    @classmethod
    def generate_application_commands(mcs) -> models.ApplicationCommand.S:
        application_commands: list[models.ApplicationCommand] = []

        for key, value in mcs._command_storage.items():
            application_commands.append(value._generate_application_command())

        return tuple(application_commands)


class InteractionHandlerClass(metaclass=_InteractionHandlerMetaClass):
    def __init__(self):
        _InteractionHandlerMetaClass.register_handler(self)


class ChatInputHandler:
    _private_parent_self: None | InteractionHandlerClass = None
    _sub_commands: dict[str, ChatInputHandler]

    @property
    def _parent_self(self) -> None | InteractionHandlerClass:
        return self._private_parent_self

    @_parent_self.setter
    def _parent_self(self, inst: InteractionHandlerClass):
        self._private_parent_self = inst
        for sub_command in self._sub_commands:
            sub_command._parent_self = inst

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
            interaction: models.Interaction,
            data_option: None | models.InteractionDataOption = None,
    ) -> models.InteractionResponse:
        assert interaction.data is not None

        options: dict[str, Any] = {}
        iterative_options = data_option.options if data_option is not None else interaction.data.options

        for option in iterative_options or ():
            if option.focused:
                return await self._auto_completes[option.name]._call(interaction, option.value)
            elif (
                    option.type == models.ApplicationCommandOptionType.SUB_COMMAND_GROUP
                    or option.type == models.ApplicationCommandOptionType.SUB_COMMAND
            ):
                return await self._sub_commands[option.name]._call(interaction, option)

            options[option.name] = option.value

        return await self.application_command(self._parent_self, interaction, **options)

    def _generate_application_command_options(self) -> tuple[models.ApplicationCommandOption, ...]:
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

            if issubclass(annotation, (enum.Enum, str)):
                annotation = str
            elif issubclass(annotation, enum.Enum):
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

            options.append(models.ApplicationCommandOption(
                type=option_type,
                name=param,
                description=param_description,
                required=required,
                autocomplete=(
                    param in self._auto_completes
                    and option_type == models.ApplicationCommandOptionType.STRING
                ) or None
            ))

        for key, value in self._sub_commands.items():
            options.append(models.ApplicationCommandOption(
                type=models.ApplicationCommandOptionType.SUB_COMMAND
                if len(value._sub_commands) == 0 else models.ApplicationCommandOptionType.SUB_COMMAND_GROUP,
                name=key,
                description=value.description[0],
                options=value._generate_application_command_options(),
            ))

        return tuple(options)

    def _generate_application_command(self) -> models.ApplicationCommand:
        return models.ApplicationCommand(
            type=models.InteractionType.APPLICATION_COMMAND,
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


class AutoCompleteHandler:
    _parent_self: None | InteractionHandlerClass = None

    def __init__(
            self,
    ):
        self.handler: None | _application_command_handler = None

    def __call__(self, handler: _application_command_handler):
        self.handler = validate_arguments(handler)

        return self

    async def _call(
            self,
            interaction: models.Interaction,
            value: str,
    ) -> models.InteractionResponse:
        return await self.handler(self._parent_self, interaction, value)


_application_command_handler = Callable[
    [InteractionHandlerClass, models.Interaction, tuple[Any, ...], dict[str, Any]],
    Coroutine[Any, Any, None | models.InteractionResponse]
]

_application_command_option_map = {
    str: models.ApplicationCommandOptionType.STRING,
    int: models.ApplicationCommandOptionType.INTEGER,
    bool: models.ApplicationCommandOptionType.BOOLEAN,
    models.User: models.ApplicationCommandOptionType.USER,
    models.Channel: models.ApplicationCommandOptionType.CHANNEL,
    models.Role: models.ApplicationCommandOptionType.ROLE,
    float: models.ApplicationCommandOptionType.NUMBER,
    models.Attachment: models.ApplicationCommandOptionType.ATTACHMENT,
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
