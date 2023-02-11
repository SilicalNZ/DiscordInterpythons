from __future__ import annotations

from dataclasses import dataclass

import aiohttp

from DiscordInterpythons.models.snowflake import ChannelID, MessageID, UserID
from DiscordInterpythons.models.model_type import AutoArchiveDuration
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.channel import Channel
from DiscordInterpythons.abcs.message import MessageABC, UpdateMessageReq
from DiscordInterpythons.utils.http_method import Method


__all__ = (
    "MessageAPI",
    "UpdateMessageReq",
)


_BASE_URL = "https://discord.com/api/v9"


@dataclass
class MessageAPI(MessageABC):
    channel_id: ChannelID
    message_id: MessageID
    token: str

    @property
    def _header_auth(self) -> dict[str, str]:
        return {"Authorization": f"Bot {self.token}"}

    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
            respond: bool = True,
    ) -> dict:
        async with aiohttp.ClientSession(
                headers={**self._header_auth},
        ) as session:
            async with session.request(
                    method.value,
                    f"{_BASE_URL}/channels/{self.channel_id}/messages/{self.message_id}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                if not (200 <= resp.status <= 299):
                    raise AssertionError(
                        f"Code: {resp.status}, URL: {_BASE_URL}/channels/{self.channel_id}/messages/{self.message_id}{endpoint}, Response: {await resp.text()}")
                if respond:
                    return await resp.json()
                return {}

    async def read(self) -> Message:
        result = await self._request(method=Method.GET)
        return Message(**result)
    
    async def create_reaction(self, emoji: str):
        await self._request(
            method=Method.PUT,
            endpoint=f"/reactions/{emoji}/@me",
        )

    async def delete_my_reaction(self, emoji: str):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/reactions/{emoji}/@me",
        )

    async def delete_user_reaction(self, user_id: UserID, emoji: str):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/reactions/{emoji}/{user_id}",
        )

    async def read_reactions_for_emoji(
            self,
            emoji: str,
            after: None | UserID = None,
            limit: None | int = None,
    ) -> tuple[User]:
        params = {}
        if after is not None:
            params["after"] = after
        if limit is not None:
            params["limit"] = limit

        result = await self._request(
            method=Method.GET,
            endpoint=f"/reactions/{emoji}",
            params=params or None,
        )
        return tuple(User(**i) for i in result)

    async def delete_all_reactions(self):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/reactions",
        )

    async def delete_all_reactions_for_emoji(self, emoji: str):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/reactions/{emoji}",
        )

    async def update(self, message: UpdateMessageReq) -> Message:
        result = await self._request(
            method=Method.PATCH,
            payload=message.dict_as_valid_json(),
        )
        return Message(**result)

    async def delete(self):
        await self._request(
            method=Method.DELETE,
        )

    async def create_crosspost(self) -> Message:
        raise NotImplementedError()

    async def create_thread(
            self,
            name: str,
            auto_archive_duration: AutoArchiveDuration | None = None,
            rate_limit_per_user: int | None = None,
    ) -> Channel:
        raise NotImplementedError()
