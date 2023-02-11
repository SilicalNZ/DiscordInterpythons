from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import aiohttp

from DiscordInterpythons.models.snowflake import ChannelID, MessageID, UserID, UserOrRoleID
from DiscordInterpythons.models.model_type import AutoArchiveDuration, ChannelType
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.channel import Channel, FollowedChannel
from DiscordInterpythons.models.permission_overwrite import PermissionOverwrite
from DiscordInterpythons.models.invite import Invite
from DiscordInterpythons.abcs.channel import (
    ChannelABC, UpdateChannelReq, CreateChannelMessageReq, CreateChannelInviteReq, ReadThreadsResp
)
from DiscordInterpythons.utils.http_method import Method


__all__ = (
    "ChannelAPI",
    "UpdateChannelReq",
    "CreateChannelMessageReq",
    "CreateChannelInviteReq",
    "ReadThreadsResp"
)


_BASE_URL = "https://discord.com/api/v9"


@dataclass
class ChannelAPI(ChannelABC):
    token: str
    channel_id: ChannelID

    @property
    def _header_auth(self) -> dict[str, str]:
        return {"Authorization": f"Bot {self.token}"}

    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            respond: bool = True,
    ) -> dict:
        async with aiohttp.ClientSession(
                headers={**self._header_auth},
        ) as session:
            async with session.request(
                    method.value,
                    f"{_BASE_URL}/channels/{self.channel_id}{endpoint}",
                    json=payload,
            ) as resp:
                if not (200 <= resp.status <= 299):
                    raise AssertionError(
                        f"Code: {resp.status}, URL: {_BASE_URL}/channels/{self.channel_id}/{endpoint}, Response: {await resp.text()}")
                if respond:
                    return await resp.json()
                return {}

    async def read(self) -> Channel:
        result = await self._request(method=Method.GET)
        return Channel(**result)

    async def delete(self):
        await self._request(method=Method.DELETE)

    async def update(self, channel: UpdateChannelReq) -> Channel:
        result = await self._request(
            method=Method.PATCH,
            payload=channel.dict_as_valid_json(),
        )
        return Channel(**result)

    async def create_typing_indicator(self):
        await self._request(
            method=Method.POST,
            endpoint="/typing",
        )

    async def create_message(self, message: CreateChannelMessageReq) -> Message:
        result = await self._request(
            method=Method.POST,
            endpoint="/messages",
            payload=message.dict_as_valid_json(),
        )
        return Message(**result)

    async def read_messages(self) -> Message.S:
        result = await self._request(
            method=Method.GET,
            endpoint="/messages",
        )
        return tuple(Message(**i) for i in result)

    async def delete_messages(self, *message_ids: tuple[MessageID]):
        await self._request(
            method=Method.DELETE,
            endpoint="/messages/bulk-delete",
            payload={"messages": message_ids},
        )

    async def update_permissions(self, permission_overwrite: PermissionOverwrite):
        await self._request(
            method=Method.PUT,
            endpoint=f"/permissions/{permission_overwrite.id}",
            payload=permission_overwrite.dict_as_valid_json(),
        )

    async def read_invites(self) -> Invite.S:
        result = await self._request(
            method=Method.GET,
            endpoint="/invites",
        )
        return tuple(Invite(**i) for i in result)

    async def create_invite(self, invite: CreateChannelInviteReq) -> Invite:
        result = await self._request(
            method=Method.POST,
            endpoint="/invites",
            payload=invite.dict_as_valid_json(),
        )
        return Invite(**result)

    async def delete_permissions(self, overwrite_id: UserOrRoleID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/permissions/{overwrite_id}",
        )

    async def create_follow_channel(self, webhook_channel_id: ChannelID) -> FollowedChannel:
        result = await self._request(
            method=Method.POST,
            endpoint="/followers",
            payload={"webhook_channel_id": webhook_channel_id},
        )
        return FollowedChannel(**result)

    async def create_pinned_message(self, message_id: MessageID):
        await self._request(
            method=Method.PUT,
            endpoint=f"/pins/{message_id}",
        )

    async def read_pinned_messages(self) -> Message.S:
        result = await self._request(
            method=Method.GET,
            endpoint="/pins",
        )
        return tuple(Message(**i) for i in result)

    async def delete_pinned_message(self, message_id: MessageID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/pins/{message_id}",
        )

    async def update_group_channel_user(self, user_id: UserID):
        raise NotImplementedError()

    async def delete_group_channel_user(self, user_id: UserID):
        raise NotImplementedError()

    async def create_thread(
            self,
            name: str,
            auto_archive_duration: AutoArchiveDuration | None = None,
            thread_type: ChannelType | None = None,
            invitable: bool | None = None,
            rate_limit_per_user: int | None = None,
    ) -> Channel:
        raise NotImplementedError()

    # async def create_thread_from_forum_channel(self) -> Channel:
    #     raise NotImplementedError()

    async def read_public_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> ReadThreadsResp:
        raise NotImplementedError()

    async def read_private_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> ReadThreadsResp:
        raise NotImplementedError()

    async def read_joined_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> ReadThreadsResp:
        raise NotImplementedError()
