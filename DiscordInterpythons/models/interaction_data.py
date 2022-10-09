from __future__ import annotations

from DiscordInterpythons.models.model_type import ApplicationCommandType, ApplicationCommandOptionType, ComponentType
from DiscordInterpythons.models.snowflake import ApplicationCommandID, UserOrMessageID, GuildID
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.guild_member import GuildMember
from DiscordInterpythons.models.role import Role
from DiscordInterpythons.models.channel import Channel
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.models._shared import _BaseModel
from DiscordInterpythons.models.component import SelectOption, ActionRow


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


class InteractionDataMessageComponent(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-message-component-data-structure

    custom_id: str
    component_type: ComponentType
    values: None | SelectOption.S


class InteractionDataModalSubmit(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-modal-submit-data-structure

    custom_id: str
    components: ActionRow.S


InteractionDataStructures = InteractionData | InteractionDataMessageComponent | InteractionDataModalSubmit
