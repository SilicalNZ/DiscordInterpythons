from __future__ import annotations

from DiscordInterpythons.models.model_type import WebhookType
from DiscordInterpythons.models.snowflake import WebhookID, GuildID, ChannelID, ApplicationID
from DiscordInterpythons.models.user import User
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "WebhookPartialGuild",
    "WebhookPartialChannel",
    "Webhook",
)


class WebhookPartialGuild(BaseModel):
    id: GuildID
    name: str
    icon: str


class WebhookPartialChannel(BaseModel):
    id: ChannelID
    name: str


class Webhook(BaseModel):
    S = tuple["Webhook", ...]

    id: WebhookID
    type: WebhookType
    guild_id: None | GuildID = None
    channel_id: None | ChannelID = None
    user: None | User = None
    name: None | str = None
    avatar: None | str = None
    token: None | str = None
    application_id: None | ApplicationID = None
    source_guild: None | WebhookPartialGuild = None
    source_channel: None | WebhookPartialChannel = None
    url: None | str = None

    _omit = {
        "guild_id",
        "user",
        "token",
        "source_guild",
        "source_channel",
        "url",
    }
