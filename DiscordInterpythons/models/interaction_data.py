from __future__ import annotations

from DiscordInterpythons.models.model_type import ApplicationCommandType, ApplicationCommandOptionType, ComponentType
from DiscordInterpythons.models.snowflake import (
    ApplicationCommandID, UserOrMessageID, GuildID, UserID, ChannelID, RoleID, MessageID, AttachmentID
)
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.guild_member import GuildMember
from DiscordInterpythons.models.role import Role
from DiscordInterpythons.models.channel import PartialChannel
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.utils.base import BaseModel
from DiscordInterpythons.models.component import SelectOption, ActionRow


__all__ = (
    "InteractionDataOption",
    "InteractionResolvedData",
    "InteractionData",
    "InteractionDataMessageComponent",
    "InteractionDataModalSubmit",
    "InteractionDataStructures",
)


class InteractionDataOption(BaseModel):
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


class InteractionResolvedData(BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure

    users: None | dict[UserID, User]
    members: None | dict[UserID, GuildMember]
    roles: None | dict[RoleID, Role]
    channels: None | dict[ChannelID, PartialChannel]
    messages: None | dict[MessageID, Message]
    attachments: None | dict[AttachmentID, Attachment]

    _omit = {
        "users",
        "members",
        "roles",
        "channels",
        "messages",
        "attachments",
    }


class InteractionData(BaseModel):
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


class InteractionDataMessageComponent(BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-message-component-data-structure

    custom_id: str
    component_type: ComponentType
    values: None | SelectOption.S


class InteractionDataModalSubmit(BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-modal-submit-data-structure

    custom_id: str
    components: ActionRow.S


InteractionDataStructures = InteractionData | InteractionDataMessageComponent | InteractionDataModalSubmit
