from __future__ import annotations

from dataclasses import dataclass
import abc

from DiscordInterpythons import models


@dataclass
class ThreadAPI(metaclass=abc.ABCMeta):
    channel_id: models.ChannelID

    # https://discord.com/developers/docs/resources/channel#join-thread
    @abc.abstractmethod
    async def create_my_member(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#add-thread-member
    @abc.abstractmethod
    async def create_member(self, user_id: models.UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#leave-thread
    @abc.abstractmethod
    async def delete_my_member(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#remove-thread-member
    @abc.abstractmethod
    async def delete_member(self, user_id: models.UserID):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#get-thread-member
    @abc.abstractmethod
    async def read_member(self, user_id: models.UserID) -> models.ThreadMember:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/channel#list-thread-members
    @abc.abstractmethod
    async def read_members(self) -> models.ThreadMember.S:
        raise NotImplementedError()
