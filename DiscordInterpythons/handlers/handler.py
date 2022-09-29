from __future__ import annotations

import enum
import types
import typing
from typing import Callable, Coroutine, Any
import inspect

from pydantic import validate_arguments

from DiscordInterpythons import models


class _InteractionHandlerMetaClass(type):
    _cls_storage: dict[InteractionHandlerClass, list[InteractionHandler, ...]] = {}
    _command_storage: dict[str, InteractionHandler] = {}

    def __new__(mcs, name, bases, attrs, **kwargs):
        cls = super().__new__(mcs, name, bases, attrs)

        if name == "InteractionHandlerClass":
            return cls

        mcs._cls_storage[cls] = []
        for name, method in attrs.items():
            if isinstance(method, InteractionHandler):
                mcs._command_storage[method.name] = method
                mcs._cls_storage[cls].append(method)

        return cls

    @classmethod
    def register_handler(mcs, inst: InteractionHandlerClass):
        for i in mcs._cls_storage[type(inst)]:
            i.parent_self = inst

    @classmethod
    async def call(mcs, interaction: models.Interaction):
        handler = mcs._command_storage.get(interaction.data.name)

        assert handler

        return await handler._call(interaction)


class InteractionHandlerClass(metaclass=_InteractionHandlerMetaClass):
    pass


class InteractionHandler:
    TYPE = models.ApplicationCommandType
    parent_self: None | InteractionHandlerClass = None
    _params: dict[str, None]
    _sub_commands: dict[str, InteractionHandler]
    sub_command_parent: None | InteractionHandler = None

    def __init__(
            self,
            type: models.ApplicationCommandType = models.ApplicationCommandType.CHAT_INPUT,
            name: None | str = None,
            sub_command_parent: None | InteractionHandler = None,
    ):
        self.application_command: None | _application_command_handler = None
        self.type = type
        self._name = name
        self._params = {}
        self._sub_commands = {}
        self.sub_command_parent = sub_command_parent

    def __call__(self, application_command: _application_command_handler):
        self.application_command = validate_arguments(application_command)

        if self.sub_command_parent:
            self.sub_command_parent._sub_commands[self.name] = self

        return self

    @property
    def name(self) -> str:
        return self._name or self.application_command.__name__

    async def _sub_command_call(
            self,
            interaction: models.Interaction,
            data_option: models.InteractionDataOption
    ) -> models.InterationResponse:
        options: dict[str, Any] = self._params.copy()

        if data_option.options is not None:
            for option in interaction.data.options:
                if option.type == models.ApplicationCommandOptionType.SUB_COMMAND:
                    return await self._sub_commands[option.name]._sub_command_call(interaction, option)

                assert option.name in options
                options[option.name] = option.value

        return await self.application_command(self.parent_self, interaction, **options)

    async def _call(
            self,
            interaction: models.Interaction
    ) -> models.InterationResponse:
        assert interaction.data is not None

        options: dict[str, Any] = self._params.copy()

        if interaction.data.options is not None:
            for option in interaction.data.options:
                if option.type == models.ApplicationCommandOptionType.SUB_COMMAND:
                    return await self._sub_commands[option.name]._sub_command_call(interaction, option)

                assert option.name in options
                options[option.name] = option.value

        return await self.application_command(self.parent_self, interaction, **options)

    def _generate_application_command_options(self) -> tuple[models.ApplicationCommandOption, ...]:
        description, param_descriptions = doc_parser(self.application_command.__doc__)

        func_annotations = inspect.get_annotations(self.application_command, eval_str=True)

        if "self" in func_annotations:
            func_annotations.pop("self")
        if "ctx" in func_annotations:
            func_annotations.pop("ctx")
        if "context" in func_annotations:
            func_annotations.pop("context")

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
            ))

            self._params[param] = None

        for key, value in self._sub_commands.items():
            options.append(models.ApplicationCommandOption(
                type=models.ApplicationCommandOptionType.SUB_COMMAND,
                name=key,
                description=value.description[0],
                option=value._generate_application_command_options(),
            ))

        return tuple(options)

    def _generate_application_command(self) -> models.ApplicationCommand:
        return models.ApplicationCommand(
            type=self.type,
            name=self.name,
            description=self.description[0],
            options=self._generate_application_command_options(),
        )

    def sub_command(
            self,
            name: None | str = None,
    ) -> InteractionHandler:
        handler = InteractionHandler(name=name, sub_command_parent=self)
        return handler

    @property
    def description(self) -> tuple[str, dict[str, str]]:
        return doc_parser(self.application_command.__doc__)


def register_handler(inst: InteractionHandlerClass):
    _InteractionHandlerMetaClass.register_handler(inst)


_application_command_handler = Callable[
    [InteractionHandlerClass, models.Interaction, tuple[Any, ...], dict[str, Any]],
    Coroutine[Any, Any, None | models.InterationResponse]
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


def doc_parser(doc_string: str) -> tuple[str, dict[str, str]]:
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
