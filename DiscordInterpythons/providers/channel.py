from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import aiohttp

from DiscordInterpythons import models
from DiscordInterpythons.abcs import channel as abc
from DiscordInterpythons.providers._shared import Method


_BASE_URL = "https://discord.com/api/v9"


@dataclass
class ChannelAPI(abc.ChannelABC):
    token: str
    channel_id: models.ChannelID

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

    async def read(self) -> models.Channel:
        result = await self._request(method=Method.GET)
        return models.Channel(**result)

    async def delete(self):
        await self._request(method=Method.DELETE)

    async def update(self, channel: abc.UpdateChannelReq) -> models.Channel:
        result = await self._request(
            method=Method.PATCH,
            payload=channel.dict_as_valid_json(),
        )
        return models.Channel(**result)

    async def create_typing_indicator(self):
        await self._request(
            method=Method.POST,
            endpoint="/typing",
        )

    async def create_message(self, message: abc.CreateChannelMessageReq) -> models.Message:
        result = await self._request(
            method=Method.POST,
            endpoint="/messages",
            payload=message.dict_as_valid_json(),
        )
        return models.Message(**result)

    async def read_messages(self) -> models.Message.S:
        result = await self._request(
            method=Method.GET,
            endpoint="/messages",
        )
        return tuple(models.Message(**i) for i in result)

    async def delete_messages(self, *message_ids: tuple[models.MessageID]):
        await self._request(
            method=Method.DELETE,
            endpoint="/messages/bulk-delete",
            payload={"messages": message_ids},
        )

    async def update_permissions(self, permission_overwrite: models.PermissionOverwrite):
        await self._request(
            method=Method.PUT,
            endpoint=f"/permissions/{permission_overwrite.id}",
            payload=permission_overwrite.dict_as_valid_json(),
        )

    async def read_invites(self) -> models.Invite.S:
        result = await self._request(
            method=Method.GET,
            endpoint="/invites",
        )
        return tuple(models.Invite(**i) for i in result)

    async def create_invite(self, invite: abc.CreateChannelInvite) -> models.Invite:
        result = await self._request(
            method=Method.POST,
            endpoint="/invites",
            payload=invite.dict_as_valid_json(),
        )
        return models.Invite(**result)

    async def delete_permissions(self, overwrite_id: models.UserOrRoleID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/permissions/{overwrite_id}",
        )

    async def create_follow_channel(self, webhook_channel_id: models.ChannelID) -> models.FollowedChannel:
        result = await self._request(
            method=Method.POST,
            endpoint="/followers",
            payload={"webhook_channel_id": webhook_channel_id},
        )
        return models.FollowedChannel(**result)

    async def create_pinned_message(self, message_id: models.MessageID):
        await self._request(
            method=Method.PUT,
            endpoint=f"/pins/{message_id}",
        )

    async def read_pinned_messages(self) -> models.Message.S:
        result = await self._request(
            method=Method.GET,
            endpoint="/pins",
        )
        return tuple(models.Message(**i) for i in result)

    async def delete_pinned_message(self, message_id: models.MessageID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/pins/{message_id}",
        )

    async def update_group_channel_user(self, user_id: models.UserID):
        raise NotImplementedError()

    async def delete_group_channel_user(self, user_id: models.UserID):
        raise NotImplementedError()

    async def create_thread(
            self,
            name: str,
            auto_archive_duration: models.AutoArchiveDuration | None = None,
            thread_type: models.ChannelType | None = None,
            invitable: bool | None = None,
            rate_limit_per_user: int | None = None,
    ) -> models.Channel:
        raise NotImplementedError()

    # async def create_thread_from_forum_channel(self) -> models.Channel:
    #     raise NotImplementedError()

    async def read_public_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> abc.ReadThreadsResp:
        raise NotImplementedError()

    async def read_private_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> abc.ReadThreadsResp:
        raise NotImplementedError()

    async def read_joined_archived_threads(
            self,
            before: datetime | None = None,
            limit: int | None = None,
    ) -> abc.ReadThreadsResp:
        raise NotImplementedError()
