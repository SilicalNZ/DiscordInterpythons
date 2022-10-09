from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import aiohttp

from DiscordInterpythons import models
from DiscordInterpythons.abcs import message as abc
from DiscordInterpythons.providers._shared import Method


_BASE_URL = "https://discord.com/api/v9"


@dataclass
class MessageAPI(abc.MessageABC):
    channel_id: models.ChannelID
    message_id: models.MessageID
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

    async def read(self) -> models.Message:
        result = await self._request(method=Method.GET)
        return models.Message(**result)
    
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

    async def delete_user_reaction(self, user_id: models.UserID, emoji: str):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/reactions/{emoji}/{user_id}",
        )

    async def read_reactions_for_emoji(
            self,
            emoji: str,
            after: None | models.UserID = None,
            limit: None | int = None,
    ) -> tuple[models.User]:
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
        return tuple(models.User(**i) for i in result)

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

    async def update(self, message: abc.UpdateMessageReq) -> models.Message:
        result = await self._request(
            method=Method.PATCH,
            payload=message.dict_as_valid_json(),
        )
        return models.Message(**result)

    async def delete(self):
        await self._request(
            method=Method.DELETE,
        )

    async def create_crosspost(self) -> models.Message:
        raise NotImplementedError()

    async def create_thread(
            self,
            name: str,
            auto_archive_duration: models.AutoArchiveDuration | None = None,
            rate_limit_per_user: int | None = None,
    ) -> models.Channel:
        raise NotImplementedError()
