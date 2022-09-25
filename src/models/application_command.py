from __future__ import annotations

from src.models.snowflake import ApplicationCommandID, ApplicationID, GuildID, Version
from src.models.model_type import ApplicationCommandType, Locale, ApplicationCommandOptionType, ChannelTypes
from src.models.flag import Permissions
from src.models._shared import _BaseModel


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

    type: None | ApplicationCommandType
    name: str
    description: str
    version: None | Version
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
        "guild_id",
        "name_localizations",
        "description_localizations",
        "options",
        "dm_permission",
        "default_permission",
    }
