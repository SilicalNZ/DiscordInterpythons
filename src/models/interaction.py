from __future__ import annotations

from src.models.snowflake import InteractionID, ApplicationID, ChannelID, GuildID
from src.models.model_type import InteractionType, Locale, InteractionResponseType
from src.models.interaction_data import InteractionData
from src.models.guild_member import GuildMember
from src.models.user import User
from src.models.message import Message
from src.models.embed import Embed
from src.models.allowed_mention import AllowedMention
from src.models.flag import MessageFlags
from src.models.component import Components
from src.models.attachment import Attachment
from src.models._shared import _BaseModel


class InteractionToken(str):
    pass


class InteractionCallbackData(_BaseModel):
    tts: None | bool = None
    content: None | str = None
    embeds: None | Embed.S = None
    allowed_mentions: None | AllowedMention.S = None
    flags: None | MessageFlags = None
    components: None | Components = None
    attachments: None | Attachment.S = None


class InterationResponse(_BaseModel):
    type: InteractionResponseType = None
    data: None | InteractionCallbackData = None


class Interaction(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interactions

    id: InteractionID
    application_id: ApplicationID
    type: InteractionType
    data: None | InteractionData
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
        if self.data is None:
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
