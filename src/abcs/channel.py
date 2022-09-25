from __future__ import annotations

from dataclasses import dataclass
import abc
from datetime import datetime

from src import models
from src.models._shared import _BaseModel


class ReadThreadsResp(_BaseModel):
    threads: models.Channel.S
    members: models.ThreadMember.S
    has_more: bool


class UpdateChannelReq(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#modify-channel-json-params-guild-channel

    name: str
    type: models.ChannelType
    position: None | int = None
    topic: None | str = None
    nsfw: None | bool = None
    rate_limit_per_user: None | int = None
    bitrate: None | int = None
    user_limit: None | int = None
    permission_overwrites: None | models.PermissionOverwrite = None
    parent_id: None | models.ChannelID = None
    rtc_region: None | str = None
    video_quality_mode: None | models.VideoQualityModes = None
    default_auto_archive_duration: None | models.AutoArchiveDuration = None


class CreateChannelMessageReq(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#create-message-jsonform-params

    content: None | str
    tts: None | bool
    embeds: None | models.Embed.S
    allowed_mentions: None | models.AllowedMention
    message_reference: None | models.MessageReference
    components: None | models.Components
    sticker_ids: None | tuple[models.StickerID, ...]
    # files: None |
    payload_json: None | str
    attachments: None | models.Attachment.S
    flags: None | models.MessageFlags

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


class CreateChannelInvite(_BaseModel):
    max_age: int
    max_uses: int
    temporary: bool
    unique: bool
    target_type: models.InviteTargetType
    target_user_id: None | models.UserID
    target_application_id: None | models.ApplicationID

    _omit = {
        "target_user_id",
        "target_application_id",
    }


@dataclass
class ChannelABC(metaclass=abc.ABCMeta):
    channel_id: models.ChannelID

    # https://discord.com/developers/docs/resources/channel#get-channel
    @abc.abstractmethod
    async def read(self) -> models.Channel:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#deleteclose-channel
    @abc.abstractmethod
    async def delete(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#modify-channel
    @abc.abstractmethod
    async def update(self, req: UpdateChannelReq) -> models.Channel:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#trigger-typing-indicator
    @abc.abstractmethod
    async def create_typing_indicator(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#create-message
    @abc.abstractmethod
    async def create_message(self, message: CreateChannelMessageReq) -> models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-channel-messages
    @abc.abstractmethod
    async def read_messages(self) -> models.Message.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#bulk-delete-messages
    @abc.abstractmethod
    async def delete_messages(self, *message_ids: tuple[models.MessageID]):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#edit-channel-permissions
    @abc.abstractmethod
    async def update_permissions(self, permission_overwrite: models.PermissionOverwrite):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-channel-invites
    @abc.abstractmethod
    async def read_invites(self) -> models.Invite.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#create-channel-invite
    @abc.abstractmethod
    async def create_invite(self, invite: CreateChannelInvite) -> models.Invite:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-channel-permission
    @abc.abstractmethod
    async def delete_permissions(self, overwrite_id: models.UserOrRoleID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#follow-news-channel
    @abc.abstractmethod
    async def create_follow_channel(self, webhook_channel_id: models.ChannelID) -> models.FollowedChannel:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#pin-message
    @abc.abstractmethod
    async def create_pinned_message(self, message_id: models.MessageID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-pinned-messages
    @abc.abstractmethod
    async def read_pinned_messages(self) -> models.Message.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#unpin-message
    @abc.abstractmethod
    async def delete_pinned_message(self, message_id: models.MessageID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#group-dm-add-recipient
    @abc.abstractmethod
    async def update_group_channel_user(self, user_id: models.UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#group-dm-remove-recipient
    @abc.abstractmethod
    async def delete_group_channel_user(self, user_id: models.UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#start-thread-without-message
    @abc.abstractmethod
    async def create_thread(
            self,
            name: str,
            auto_archive_duration: models.AutoArchiveDuration | None = None,
            thread_type: models.ChannelType | None = None,
            invitable: bool | None = None,
            rate_limit_per_user: int | None = None,
    ) -> models.Channel:
        raise NotImplementedError()

    # # https://discord.com/developers/docs/resources/channel#start-thread-in-forum-channel
    # @abcs.abstractmethod
    # async def create_thread_from_forum_channel(self) -> models.Channel:
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
