from __future__ import annotations

from dataclasses import dataclass
import abc

from DiscordInterpythons import models
from DiscordInterpythons.models._shared import _BaseModel


class UpdateMessageReq(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#edit-message-jsonform-params
    content: None | str = None
    embeds: None | models.Embed.S = None
    flags: None | models.Permissions = None
    allowed_mentions: None | models.AllowedMention = None
    components: None | tuple[models.ActionRow, ...] = None
    # files = None
    payload_json: None | str = None
    attachments: None | models.Attachment.S = None

    _omit = {
        "content",
        "embeds",
        "flags",
        "allowed_mentions",
        "components",
        "payload_json",
        "attachments",
    }


@dataclass
class MessageABC(metaclass=abc.ABCMeta):
    channel_id: models.ChannelID
    message_id: models.MessageID

    # https://discord.com/developers/docs/resources/channel#get-channel-message
    @abc.abstractmethod
    async def read(self) -> models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#create-reaction
    @abc.abstractmethod
    async def create_reaction(self, emoji: str):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-own-reaction
    @abc.abstractmethod
    async def delete_my_reaction(self, emoji: str):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-user-reaction
    @abc.abstractmethod
    async def delete_user_reaction(self, user_id: models.UserID, emoji: str):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-reactions
    @abc.abstractmethod
    async def read_reactions_for_emoji(
            self,
            emoji: str,
            after: None | models.UserID = None,
            limit: None | int = None,
    ) -> tuple[models.User]:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-all-reactions
    @abc.abstractmethod
    async def delete_all_reactions(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-all-reactions-for-emoji
    @abc.abstractmethod
    async def delete_all_reactions_for_emoji(self, emoji: str):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#edit-message
    @abc.abstractmethod
    async def update(self, message: UpdateMessageReq) -> models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-message
    @abc.abstractmethod
    async def delete(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#crosspost-message
    @abc.abstractmethod
    async def create_crosspost(self) -> models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#start-thread-from-message
    @abc.abstractmethod
    async def create_thread(
            self,
            name: str,
            auto_archive_duration: models.AutoArchiveDuration | None = None,
            rate_limit_per_user: int | None = None,
    ) -> models.Channel:
        raise NotImplementedError()
