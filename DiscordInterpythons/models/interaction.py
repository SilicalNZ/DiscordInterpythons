from __future__ import annotations

from DiscordInterpythons.models.snowflake import InteractionID, ApplicationID, ChannelID, GuildID
from DiscordInterpythons.models.model_type import InteractionType, Locale, InteractionResponseType
from DiscordInterpythons.models.interaction_data import InteractionData, InteractionDataStructures
from DiscordInterpythons.models.guild_member import GuildMember
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.embed import Embed
from DiscordInterpythons.models.allowed_mention import AllowedMention
from DiscordInterpythons.models.flag import MessageFlags
from DiscordInterpythons.models.component import ActionRow
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.models._shared import _BaseModel
from DiscordInterpythons.models.application_command import ApplicationCommandOptionChoice


class InteractionToken(str):
    pass


class InteractionCallbackData(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure

    tts: None | bool = None
    content: None | str = None
    embeds: None | Embed.S = None
    allowed_mentions: None | AllowedMention.S = None
    flags: None | MessageFlags = None
    components: None | ActionRow.S = None
    attachments: None | Attachment.S = None

    # TODO: These should be their own classes
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-autocomplete
    choices: None | tuple[ApplicationCommandOptionChoice, ...] = None

    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-modal
    custom_id: None | str = None
    title: None | str = None

    _omit = {
        "tts",
        "content",
        "embeds",
        "allowed_mentions",
        "flags",
        "components",
        "attachments",
        "choices",
        "custom_id",
        "title",
    }


class InteractionResponse(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-response-structure

    type: InteractionResponseType
    data: None | InteractionCallbackData = None

    _omit = {
        "data"
    }


class Interaction(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interactions

    id: InteractionID
    application_id: ApplicationID
    type: InteractionType
    data: None | InteractionDataStructures
    guild_id: None | GuildID
    channel_id: None | ChannelID
    member: None | GuildMember
    user: None | User
    token: InteractionToken
    version: int
    message: None | Message
    locale: None | Locale
    guild_locale: None | Locale

    def get_sub_command(self) -> None | InteractionData:
        if self.data is None and not isinstance(self.data, InteractionData):
            return None

        return self.data.get_sub_command()

    _omit = {
        "data",
        "guild_id",
        "channel_id",
        "member",
        "user",
        "message",
        "app_permissions",
        "locale",
        "guild_locale",
    }
