from __future__ import annotations

from typing import Sequence

from DiscordInterpythons.models.snowflake import ApplicationCommandID, ApplicationID, GuildID, Version
from DiscordInterpythons.models.model_type import ApplicationCommandType, Locale, ApplicationCommandOptionType, ChannelTypes
from DiscordInterpythons.models.flag import Permissions
from DiscordInterpythons.models._shared import _BaseModel


class ApplicationCommandOptionChoice(_BaseModel):
    # https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure

    S = tuple["ApplicationCommandOptionChoice", ...]

    name: str
    value: str | int | float
    name_localizations: None | dict[Locale, str] = None

    _omit = {
        "name_localizations",
    }

    def is_different(self, other: ApplicationCommandOptionChoice) -> bool:
        assert other.name == self.name

        if other.value != self.value:
            return True
        elif _is_empty(other.name_localizations) != _is_empty(self.name_localizations):
            return True
        elif (other.name_localizations is not None and self.name_localizations is not None) \
                and other.name_localizations != self.name_localizations:
            return True

        return False


class ApplicationCommandOption(_BaseModel):
    # https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure

    S = tuple["ApplicationCommandOption", ...]

    type: ApplicationCommandOptionType
    name: str
    description: str
    name_localizations: None | dict[Locale, str] = None
    description_localizations: None | dict[Locale, str] = None
    required: None | bool = None
    choices: None | ApplicationCommandOptionChoice.S = None
    options: None | tuple["ApplicationCommandOption", ...] = None
    channel_types: None | ChannelTypes = None
    min_value: None | int | float = None
    max_value: None | int | float = None
    autocomplete: None | bool = None

    _omit = {
        "name_localizations",
        "description_localizations",
        "required",
        "choices",
        "options",
        "channel_types",
        "min_value",
        "max_value",
        "min_length",
        "max_length",
        "autocomplete",
    }

    def is_different(self, other: ApplicationCommandOption) -> bool:
        assert other.name == self.name

        if other.type != self.type:
            return True
        elif other.description != self.description:
            return True
        elif _is_empty(other.name_localizations) != _is_empty(self.name_localizations):
            return True
        elif (other.name_localizations is not None and self.name_localizations is not None) \
                and other.name_localizations != self.name_localizations:
            return True
        elif _is_empty(other.description_localizations) != _is_empty(self.description_localizations):
            return True
        elif (other.description_localizations is not None and self.description_localizations is not None) \
                and other.description_localizations != self.description_localizations:
            return True
        elif other.required != self.required:
            return True
        elif len(other.options or []) != len(self.options or []):
            return True

        def sort_lamb(option: ApplicationCommandOption | ApplicationCommandOptionChoice):
            return option.name

        for x, y in zip(sorted(other.options or [], key=sort_lamb), sorted(self.options or [], key=sort_lamb)):
            if x.name != y.name:
                return True
            if x.is_different(y):
                return True

        if len(other.choices or []) != len(self.choices or []):
            return True

        for x, y in zip(sorted(other.choices or [], key=sort_lamb), sorted(self.choices or [], key=sort_lamb)):
            if x.name != y.name:
                return True
            if x.is_different(y):
                return True

        if len(other.channel_types or []) != len(self.options or []):
            return True

        for x, y in zip(sorted(other.channel_types or []), sorted(self.channel_types or [])):
            if x != y:
                return True

        if other.min_value != self.min_value:
            return True
        elif other.max_value != self.max_value:
            return True
        elif other.autocomplete != self.autocomplete:
            return True

        return False


class ApplicationCommand(_BaseModel):
    # https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure

    S = tuple["ApplicationCommand", ...]

    name: str
    description: str
    type: None | ApplicationCommandType = None
    version: None | Version = None
    options: None | ApplicationCommandOption.S = None
    id: None | ApplicationCommandID = None
    application_id: None | ApplicationID = None
    guild_id: None | GuildID = None
    name_localizations: None | dict[Locale, str] = None
    description_localizations: None | dict[Locale, str] = None
    default_member_permissions: None | Permissions = None
    dm_permission: None | bool = None

    _omit = {
        "type",
        "version",
        "options",
        "id",
        "application_id",
        "guild_id",
        "name_localizations",
        "description_localizations",
        "default_member_permissions",
        "dm_permission",
    }

    def is_different(self, other: ApplicationCommand) -> bool:
        assert other.name == self.name

        if other.description != self.description:
            return True
        elif other.dm_permission != self.dm_permission:
            return True
        elif len(other.options or []) != len(self.options or []):
            return True

        def sort_lamb(option: ApplicationCommandOption):
            return option.name

        for x, y in zip(sorted(other.options or [], key=sort_lamb), sorted(self.options or [], key=sort_lamb)):
            if x.name != y.name:
                return True
            if x.is_different(y):
                return True

        return False


def _is_empty(value: None | Sequence) -> bool:
    return value is None or len(value) == 0
