from __future__ import annotations

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
        elif ((other.options is None and self.options is not None)
                or (other.options is not None and self.options is None)
                or ((other.options is not None and len(other.options) == 0)
                    and (self.options is not None and len(self.options) == 0))):
            return False
        elif len(other.options) != len(other.options):
            return True

        def sort_lamb(option: ApplicationCommandOption):
            return option.name

        for x, y in zip(sorted(other.options, key=sort_lamb), sorted(other.options, key=sort_lamb)):
            if x != y:
                return True
        return False
