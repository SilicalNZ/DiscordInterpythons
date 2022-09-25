from __future__ import annotations

from src.models.model_type import ApplicationCommandType, ApplicationCommandOptionType
from src.models.snowflake import ApplicationCommandID, UserOrMessageID, GuildID
from src.models.user import User
from src.models.guild_member import GuildMember
from src.models.role import Role
from src.models.channel import Channel
from src.models.message import Message
from src.models.attachment import Attachment
from src.models._shared import _BaseModel


class InteractionDataOption(_BaseModel):
    # https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-interaction-data-option-structure

    S = tuple["InteractionDataOption", ...]

    name: str
    type: ApplicationCommandOptionType
    value: None | str | int | float
    options: None | tuple[InteractionDataOption, ...]
    focused: None | bool

    _omit = {
        "value",
        "options",
        "focused",
    }


class InteractionResolvedData(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure

    users: None | User.S
    members: None | GuildMember.S
    roles: None | Role.S
    channels: None | Channel.S
    messages: None | Message.S
    attachments: None | Attachment.S

    _omit = {
        "users",
        "members",
        "roles",
        "channels",
        "messages",
        "attachments",
    }


class InteractionData(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-application-command-data-structure

    id: ApplicationCommandID
    name: str
    type: ApplicationCommandType
    resolved: None | InteractionResolvedData
    options: None | InteractionDataOption.S
    guild_id: None | GuildID
    target_id: None | UserOrMessageID

    def get_sub_command(self) -> None | InteractionDataOption:
        if self.options is None or len(self.options) != 1:
            return None

        subcommand = self.options[0]

        if subcommand.type != ApplicationCommandOptionType.SUB_COMMAND:
            return None

        return subcommand

    _omit = {
        "resolved",
        "options",
        "guild_id",
        "target_id",
    }
