from __future__ import annotations

from datetime import datetime

from DiscordInterpythons.models.snowflake import ThreadID, GuildID, ChannelID, ApplicationID, WebhookID
from DiscordInterpythons.models.flag import ChannelFlag
from DiscordInterpythons.models.model_type import ChannelType, AutoArchiveDuration
from DiscordInterpythons.models._shared import _BaseModel
from DiscordInterpythons.models.permission_overwrite import Permissions, PermissionOverwrite
from DiscordInterpythons.models.user import UserID, User


class ThreadMetaData(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#thread-metadata-object-thread-metadata-structure

    archived: bool
    auto_archive_duration: AutoArchiveDuration
    archive_timestamp: datetime
    locked: bool
    invitable: None | bool
    create_timestamp: None | datetime

    _omit = {
        "invitable",
        "create_timestamp",
    }


class ThreadMember(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#thread-member-object-thread-member-structure

    S = tuple["ThreadMember", ...]

    id: ThreadID
    user_id: UserID
    join_timestamp: datetime
    flags: int


class ChannelMention(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#channel-mention-object-channel-mention-structure

    S = tuple["ChannelMention", ...]

    id: ChannelID
    guild_id: GuildID
    type: ChannelType
    name: str


class Channel(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#channel-object

    S = tuple["Channel", ...]

    id: ChannelID
    type: ChannelType
    guild_id: None | GuildID
    position: None | int
    permission_overwrites: None | PermissionOverwrite.S
    name: None | str
    topic: None | str
    nsfw: None | str
    last_message_id: None | bool
    bitrate: None | int
    user_limit: None | int
    rate_limit_per_user: None | int
    recipients: None | User.S
    icon: None | str
    owner_id: None | UserID
    application_id: None | ApplicationID
    parent_id: None | ChannelID
    last_pin_timestamp: datetime
    rtc_region: None | str
    video_quality_mode: None | int
    message_count: None | int
    member_count: None | int
    thread_metadata: None | int
    member: None | ThreadMember
    default_auto_archive_duration: int
    permissions: Permissions
    flags: None | ChannelFlag

    _omit = {
        "guild_id",
        "position",
        "permission_overwrites",
        "name",
        "topic",
        "nsfw",
        "last_message_id",
        "bitrate",
        "user_limit",
        "rate_limit_per_user",
        "recipients",
        "icon",
        "owner_id",
        "application_id",
        "parent_id",
        "last_pin_timestamp",
        "rtc_region",
        "video_quality_mode",
        "message_count",
        "member_count",
        "thread_metadata",
        "member",
        "default_auto_archive_duration",
        "permissions",
        "flags",
        "total_message_sent",
    }


class FollowedChannel(_BaseModel):
    channel_id: ChannelID
    webhook_id: WebhookID
