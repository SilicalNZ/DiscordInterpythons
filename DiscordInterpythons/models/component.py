from __future__ import annotations

from DiscordInterpythons.models.model_type import ComponentType, ButtonStyleType, TextInputStyleType
from DiscordInterpythons.models.emoji import PartialEmoji
from DiscordInterpythons.models._shared import _BaseModel


class Button(_BaseModel):
    # https://discord.com/developers/docs/interactions/message-components#button-object

    S = tuple["Button", ...]

    type: ComponentType
    style: ButtonStyleType
    label: None | str
    emoji: None | PartialEmoji
    custom_id: None | str
    url: None | str
    disabled: None | bool


class SelectOption(_BaseModel):
    # https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-option-structure

    S = tuple["SelectOption", ...]

    label: str
    value: str
    description: None | str = None
    emoji: None | PartialEmoji = None
    default: None | bool = None


class SelectMenu(_BaseModel):
    # https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-menu-structure

    type: ComponentType
    custom_id: str
    options: SelectOption.S
    placeholder: None | str
    min_values: None | int
    max_values: None | int
    disabled: None | bool


class TextInput(_BaseModel):
    # https://discord.com/developers/docs/interactions/message-components#text-inputs-text-input-structure

    type: ComponentType
    custom_id: str
    style: TextInputStyleType
    label: str
    min_length: None | int
    max_length: None | int
    required: bool
    value: str
    placeholder: str


class ActionRow(_BaseModel):
    # https://discord.com/developers/docs/interactions/message-components#text-inputs-text-input-styles

    S = tuple["ActionRow", ...]

    type: ComponentType
    components: ActionRowComponents


def cast_components(array: tuple[dict, ...]) -> Components:
    results: list[Component] = []

    for i in array:
        if i["type"] == ComponentType.ACTION_ROW:
            results.append(ActionRow(**i))
        elif i["type"] == ComponentType.BUTTON:
            results.append(Button(**i))
        elif i["type"] == ComponentType.SELECT_MENU:
            results.append(SelectMenu(**i))
        elif i["type"] == ComponentType.TEXT_INPUT:
            results.append(TextInput(**i))
        else:
            # TODO: Make this anonymous
            raise AssertionError("Could not Convert type")

    return tuple(results)


def cast_action_row_components(array: tuple[dict, ...]) -> ActionRowComponents:
    results: list[ActionRowComponent] = []

    for i in array:
        if i["type"] == ComponentType.BUTTON:
            results.append(Button(**i))
        elif i["type"] == ComponentType.SELECT_MENU:
            results.append(SelectMenu(**i))
        elif i["type"] == ComponentType.TEXT_INPUT:
            results.append(TextInput(**i))
        else:
            # TODO: Make this anonymous
            raise AssertionError("Could not Convert type")

    return tuple(results)


ActionRowComponent = Button | SelectMenu | TextInput
ActionRowComponents = tuple[ActionRowComponent, ...]
Component = Button | SelectMenu | TextInput | ActionRow
Components = tuple[Component, ...]
