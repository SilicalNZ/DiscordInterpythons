from __future__ import annotations

from datetime import datetime

from DiscordInterpythons.models.snowflake import RoleID, GuildID, ChannelID, InteractionID, MessageID, WebhookID, ApplicationID
from DiscordInterpythons.models.model_type import InteractionType, MessageActivityType, MessageType
from DiscordInterpythons.models.flag import MessageFlags
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.guild_member import GuildMember, PartialGuildMember
from DiscordInterpythons.models.channel import Channel, ChannelMention
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.models.embed import Embed
from DiscordInterpythons.models.reaction import Reaction
from DiscordInterpythons.models.component import ActionRow
from DiscordInterpythons.models.sticker import Sticker, PartialSticker
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "MessageInteraction",
    "MessageReference",
    "MessageActivity",
    "Message",
)


class MessageInteraction(BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#message-interaction-object-message-interaction-structure

    id: InteractionID
    type: InteractionType
    name: str
    user: User
    member: None | PartialGuildMember

    _omit = {
        "member",
    }


class MessageReference(BaseModel):
    # https://discord.com/developers/docs/resources/channel#message-reference-object-message-reference-structure

    message_id: None | MessageID
    channel_id: None | ChannelID
    guild_id: None | GuildID
    fail_if_not_exists: None | bool

    _omit = {
        "message_id",
        "channel_id",
        "guild_id",
        "fail_if_not_exists",
    }


class MessageActivity(BaseModel):
    # https://discord.com/developers/docs/resources/channel#message-object-message-activity-structure

    type: MessageActivityType
    party_id: None | str

    _omit = {
        "party_id",
    }


class Message(BaseModel):
    # https://discord.com/developers/docs/resources/channel#message-object

    S = tuple["Message", ...]

    id: MessageID
    channel_id: ChannelID
    author: User
    member: None | GuildMember
    content: str
    timestamp: datetime
    edited_timestamp: None | datetime
    tts: bool
    mention_everyone: bool
    mentions: User.S
    mention_roles: tuple[RoleID, ...]
    mention_channels: None | ChannelMention.S
    attachments: Attachment.S
    embeds: Embed.S
    reactions: None | Reaction.S
    nonce: None | int | str
    pinned: bool
    webhook_id: None | WebhookID
    type: MessageType
    activity: None | MessageActivity
    application: None | dict  # TODO: this
    application_id: None | ApplicationID
    message_reference: None | MessageReference
    flags: MessageFlags
    referenced_message: None | Message
    interaction: None | MessageInteraction
    thread: None | Channel
    components: ActionRow.S
    sticker_items: None | PartialSticker.S
    stickers: None | Sticker.S

    _omit = {
        "mention_channels",
        "reactions",
        "nonce",
        "webhook_id",
        "activity",
        "application",
        "application_id",
        "message_reference",
        "flags",
        "referenced_message",
        "interaction",
        "thread",
        "components",
        "sticker_items",
        "stickers",
        "position",
    }
