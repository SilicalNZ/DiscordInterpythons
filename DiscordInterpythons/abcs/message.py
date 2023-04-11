from __future__ import annotations

from dataclasses import dataclass
import abc

from DiscordInterpythons.models.snowflake import ChannelID, MessageID, UserID
from DiscordInterpythons.models.model_type import AutoArchiveDuration
from DiscordInterpythons.models.flag import Permissions
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.channel import Channel
from DiscordInterpythons.models.embed import Embed
from DiscordInterpythons.models.allowed_mention import AllowedMention
from DiscordInterpythons.models.component import ActionRow
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "UpdateMessageReq",
    "MessageABC",
)


class UpdateMessageReq(BaseModel):
    # https://discord.com/developers/docs/resources/channel#edit-message-jsonform-params
    content: None | str = None
    embeds: None | Embed.S = None
    flags: None | Permissions = None
    allowed_mentions: None | AllowedMention = None
    components: None | tuple[ActionRow, ...] = None
    # files = None
    # payload_json: None | str = None
    attachments: None | Attachment.S = None

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
    channel_id: ChannelID
    message_id: MessageID

    # https://discord.com/developers/docs/resources/channel#get-channel-message
    @abc.abstractmethod
    async def read(self) -> Message:
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
    async def delete_user_reaction(self, user_id: UserID, emoji: str):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-reactions
    @abc.abstractmethod
    async def read_reactions_for_emoji(
            self,
            emoji: str,
            after: None | UserID = None,
            limit: None | int = None,
    ) -> tuple[User]:
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
    async def update(self, message: UpdateMessageReq) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#delete-message
    @abc.abstractmethod
    async def delete(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#crosspost-message
    @abc.abstractmethod
    async def create_crosspost(self) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#start-thread-from-message
    @abc.abstractmethod
    async def create_thread(
            self,
            name: str,
            auto_archive_duration: AutoArchiveDuration | None = None,
            rate_limit_per_user: int | None = None,
    ) -> Channel:
        raise NotImplementedError()
