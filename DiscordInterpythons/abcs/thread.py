from __future__ import annotations

from dataclasses import dataclass
import abc

from DiscordInterpythons.models.snowflake import ChannelID, UserID
from DiscordInterpythons.models.channel import ThreadMember


__all__ = (
    "ThreadABC",
)


@dataclass
class ThreadABC(metaclass=abc.ABCMeta):
    channel_id: ChannelID

    # https://discord.com/developers/docs/resources/channel#join-thread
    @abc.abstractmethod
    async def create_my_member(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#add-thread-member
    @abc.abstractmethod
    async def create_member(self, user_id: UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#leave-thread
    @abc.abstractmethod
    async def delete_my_member(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#remove-thread-member
    @abc.abstractmethod
    async def delete_member(self, user_id: UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-thread-member
    @abc.abstractmethod
    async def read_member(self, user_id: UserID) -> ThreadMember:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#list-thread-members
    @abc.abstractmethod
    async def read_members(self) -> ThreadMember.S:
        raise NotImplementedError()
