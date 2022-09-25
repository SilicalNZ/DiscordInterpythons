from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import aiohttp

from src import models
from src.abcs import webhook as abc
from src.providers._shared import Method


_BASE_URL = "https://discord.com/api/v8/webhooks"


@dataclass
class WebhookAuthABC(abc.WebhookAuthABC):
    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
    ) -> dict:
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.request(
                    method.value,
                    f"{_BASE_URL}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                return await resp.json()

    async def create_webhook(
            self,
            channel_id: models.ChannelID,
            name: str,
            avatar: None | str = None,
    ) -> models.Webhook:
        payload = {
            "name": name,
        }

        if avatar is not None:
            payload["avatar"] = avatar

        result = await self._request(
            method=Method.POST,
            endpoint=f"/channels/{channel_id}/webhooks",
            payload=payload,
        )
        return models.Webhook(**result)

    async def read_channel_webhooks(self, channel_id: models.ChannelID) -> models.Webhook.S:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/channels/{channel_id}/webhooks",
        )
        return tuple(models.Webhook(**i) for i in result)

    async def read_guild_webhooks(self, guild_id: models.GuildID) -> models.Webhook.S:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/guilds/{guild_id}/webhooks",
        )
        return tuple(models.Webhook(**i) for i in result)

    async def read_webhook(self, webhook_id: models.WebhookID) -> models.Webhook:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{webhook_id}",
        )
        return models.Webhook(**result)

    async def update_webhook(
            self,
            webhook_id: models.WebhookID,
            name: None | str = None,
            avatar: None | str = None,
            channel_id: None | models.ChannelID = None,
    ) -> models.Webhook:
        payload = {}

        if name is not None:
            payload["name"] = name

        if avatar is not None:
            payload["avatar"] = avatar

        if channel_id is not None:
            payload["channel_id"] = channel_id

        result = await self._request(
            method=Method.PATCH,
            endpoint=f"/webhooks/{webhook_id}",
            payload=payload or None,
        )
        return models.Webhook(**result)

    async def delete_webhook(self, webhook_id: models.WebhookID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{webhook_id}",
        )


@dataclass
class WebhookABC(abc.WebhookABC):
    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict = None,
            params: None | dict = None,
    ) -> dict:
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.request(
                    method.value,
                    endpoint,
                    json=payload,
                    params=params,
            ) as resp:
                return await resp.json()

    async def read_webhook(self) -> models.Webhook:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}",
        )
        return models.Webhook(**result)

    async def update_webhook_with_token(
            self,
            name: None | str = None,
            avatar: None | str = None,
    ) -> models.Webhook:
        payload = {}

        if name is not None:
            payload["name"] = name

        if avatar is not None:
            payload["avatar"] = avatar

        result = await self._request(
            method=Method.PATCH,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}",
            payload=payload or None,
        )
        return models.Webhook(**result)

    async def delete_webhook(self):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}",
        )

    async def execute_webhook(
            self,
            message: abc.ExecuteWebhookReq,
            wait: None | bool = None,
            thread_id: None | models.ThreadID = None,
    ) -> None | models.Message:
        params = {}

        if wait is not None:
            params["wait"] = wait

        if thread_id is not None:
            params['thread_id'] = thread_id

        result = await self._request(
            method=Method.POST,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}",
            params=params or None,
            payload=message.dict(),
        )

        if wait is not None:
            return None

        return models.Message(**result)

    async def read_webhook_message(self, message_id: models.MessageID) -> models.Message:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}/messages/{message_id}",
        )

        return models.Message(**result)

    async def update_webhook_message(
            self,
            message_id: models.MessageID,
            message: abc.UpdateWebhookMessageReq,
            thread_id: None | models.ThreadID = None,
    ) -> models.Message:
        params = {}

        if thread_id is not None:
            params["thread_id"] = thread_id

        result = await self._request(
            method=Method.PATCH,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}/messages/{message_id}",
            payload=message.dict(),
            params=params,
        )

        return models.Message(**result)

    async def delete_webhook_message(
            self,
            message_id: models.MessageID,
            thread_id: None | models.ThreadID = None,
    ):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}/messages/{message_id}",
        )
