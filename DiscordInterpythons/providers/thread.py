from __future__ import annotations

from dataclasses import dataclass

from DiscordInterpythons.models.snowflake import ChannelID, UserID
from DiscordInterpythons.models.channel import ThreadMember
from DiscordInterpythons.abcs.thread import ThreadABC


__all__ = (
    "ThreadAPI",
)


@dataclass
class ThreadAPI(ThreadABC):
    channel_id: ChannelID

    async def create_my_member(self):
        raise NotImplementedError()

    async def create_member(self, user_id: UserID):
        raise NotImplementedError()

    async def delete_my_member(self):
        raise NotImplementedError()

    async def delete_member(self, user_id: UserID):
        raise NotImplementedError()

    async def read_member(self, user_id: UserID) -> ThreadMember:
        raise NotImplementedError()

    async def read_members(self) -> ThreadMember.S:
        raise NotImplementedError()
