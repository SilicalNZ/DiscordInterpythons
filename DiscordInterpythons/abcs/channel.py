from __future__ import annotations

from dataclasses import dataclass
import abc
from datetime import datetime

from DiscordInterpythons.models.snowflake import ChannelID, MessageID, UserID, UserOrRoleID, StickerID, ApplicationID
from DiscordInterpythons.models.model_type import AutoArchiveDuration, ChannelType, VideoQualityModes, InviteTargetType
from DiscordInterpythons.models.flag import MessageFlags
from DiscordInterpythons.models.message import Message, MessageReference
from DiscordInterpythons.models.channel import Channel, FollowedChannel, ThreadMember
from DiscordInterpythons.models.permission_overwrite import PermissionOverwrite
from DiscordInterpythons.models.invite import Invite
from DiscordInterpythons.models.embed import Embed
from DiscordInterpythons.models.allowed_mention import AllowedMention
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.models.component import ActionRow
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "ChannelABC",
    "UpdateChannelReq",
    "CreateChannelMessageReq",
    "CreateChannelInviteReq",
    "ReadThreadsResp",
)


class ReadThreadsResp(BaseModel):
    threads: Channel.S
    members: ThreadMember.S
    has_more: bool


class UpdateChannelReq(BaseModel):
    # https://discord.com/developers/docs/resources/channel#modify-channel-json-params-guild-channel

    name: str
    type: ChannelType
    position: None | int = None
    topic: None | str = None
    nsfw: None | bool = None
    rate_limit_per_user: None | int = None
    bitrate: None | int = None
    user_limit: None | int = None
    permission_overwrites: None | PermissionOverwrite = None
    parent_id: None | ChannelID = None
    rtc_region: None | str = None
    video_quality_mode: None | VideoQualityModes = None
    default_auto_archive_duration: None | AutoArchiveDuration = None


class CreateChannelMessageReq(BaseModel):
    # https://discord.com/developers/docs/resources/channel#create-message-jsonform-params

    content: None | str
    tts: None | bool
    embeds: None | Embed.S
    allowed_mentions: None | AllowedMention
    message_reference: None | MessageReference
    components: None | ActionRow.S
    sticker_ids: None | tuple[StickerID, ...]
    # files: None |
    payload_json: None | str
    attachments: None | Attachment.S
    flags: None | MessageFlags

    _omit = {
        "content",
        "tts",
        "embeds",
        "allowed_mentions",
        "message_reference",
        "components",
        "sticker_ids",
        "files",
        "payload_json",
        "attachments",
        "flags",
    }


class CreateChannelInviteReq(BaseModel):
    max_age: int
    max_uses: int
    temporary: bool
    unique: bool
    target_type: InviteTargetType
    target_user_id: None | UserID
    target_application_id: None | ApplicationID

    _omit = {
        "target_user_id",
        "target_application_id",
    }


@dataclass
class ChannelABC(metaclass=abc.ABCMeta):
    channel_id: ChannelID

    # https://discord.com/developers/docs/resources/channel#get-channel
    @abc.abstractmethod
    async def read(self) -> Channel:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#deleteclose-channel
    @abc.abstractmethod
    async def delete(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#modify-channel
    @abc.abstractmethod
    async def update(self, req: UpdateChannelReq) -> Channel:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#trigger-typing-indicator
    @abc.abstractmethod
    async def create_typing_indicator(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#create-message
    @abc.abstractmethod
    async def create_message(self, message: CreateChannelMessageReq) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-channel-messages
    @abc.abstractmethod
    async def read_messages(self) -> Message.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#bulk-delete-messages
    @abc.abstractmethod
    async def delete_messages(self, *message_ids: tuple[MessageID]):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#edit-channel-permissions
    @abc.abstractmethod
    async def update_permissions(self, permission_overwrite: PermissionOverwrite):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-channel-invites
    @abc.abstractmethod
    async def read_invites(self) -> Invite.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#create-channel-invite
    @abc.abstractmethod
    async def create_invite(self, invite: CreateChannelInviteReq) -> Invite:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-channel-permission
    @abc.abstractmethod
    async def delete_permissions(self, overwrite_id: UserOrRoleID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#follow-news-channel
    @abc.abstractmethod
    async def create_follow_channel(self, webhook_channel_id: ChannelID) -> FollowedChannel:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#pin-message
    @abc.abstractmethod
    async def create_pinned_message(self, message_id: MessageID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-pinned-messages
    @abc.abstractmethod
    async def read_pinned_messages(self) -> Message.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#unpin-message
    @abc.abstractmethod
    async def delete_pinned_message(self, message_id: MessageID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#group-dm-add-recipient
    @abc.abstractmethod
    async def update_group_channel_user(self, user_id: UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#group-dm-remove-recipient
    @abc.abstractmethod
    async def delete_group_channel_user(self, user_id: UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#start-thread-without-message
    @abc.abstractmethod
    async def create_thread(
            self,
            name: str,
            auto_archive_duration: AutoArchiveDuration | None = None,
            thread_type: ChannelType | None = None,
            invitable: bool | None = None,
            rate_limit_per_user: int | None = None,
    ) -> Channel:
        raise NotImplementedError()

    # # https://discord.com/developers/docs/resources/channel#start-thread-in-forum-channel
    # @abcs.abstractmethod
    # async def create_thread_from_forum_channel(self) -> Channel:
    #     raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#list-public-archived-threads
    @abc.abstractmethod
    async def read_public_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> ReadThreadsResp:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#list-private-archived-threads
    @abc.abstractmethod
    async def read_private_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> ReadThreadsResp:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#list-joined-private-archived-threads
    @abc.abstractmethod
    async def read_joined_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> ReadThreadsResp:
        raise NotImplementedError()
