from __future__ import annotations

from dataclasses import dataclass

import aiohttp

from DiscordInterpythons.models.snowflake import (
    ChannelID, WebhookID, GuildID, ThreadID, MessageID, InteractionID, ApplicationID
)
from DiscordInterpythons.models.webhook import Webhook
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.abcs.webhook import (
    WebhookABC, WebhookAuthABC, InteractionResponseABC, ExecuteWebhookReq, UpdateWebhookMessageReq, CreateFollowupReq
)
from DiscordInterpythons.utils.http_method import Method


__all__ = (
    "WebhookAuthAPI",
    "WebhookAPI",
    "InteractionResponseAPI",
    "ExecuteWebhookReq",
    "UpdateWebhookMessageReq",
    "CreateFollowupReq",
)


_BASE_URL = "https://discord.com/api/v8"


@dataclass
class WebhookAuthAPI(WebhookAuthABC):
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
            channel_id: ChannelID,
            name: str,
            avatar: None | str = None,
    ) -> Webhook:
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
        return Webhook(**result)

    async def read_channel_webhooks(self, channel_id: ChannelID) -> Webhook.S:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/channels/{channel_id}/webhooks",
        )
        return tuple(Webhook(**i) for i in result)

    async def read_guild_webhooks(self, guild_id: GuildID) -> Webhook.S:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/guilds/{guild_id}/webhooks",
        )
        return tuple(Webhook(**i) for i in result)

    async def read_webhook(self, webhook_id: WebhookID) -> Webhook:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{webhook_id}",
        )
        return Webhook(**result)

    async def update_webhook(
            self,
            webhook_id: WebhookID,
            name: None | str = None,
            avatar: None | str = None,
            channel_id: None | ChannelID = None,
    ) -> Webhook:
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
        return Webhook(**result)

    async def delete_webhook(self, webhook_id: WebhookID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{webhook_id}",
        )


@dataclass
class WebhookAPI(WebhookABC):
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

    async def read_webhook(self) -> Webhook:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/{self.webhook_id}/{self.token}",
        )
        return Webhook(**result)

    async def update_webhook_with_token(
            self,
            name: None | str = None,
            avatar: None | str = None,
    ) -> Webhook:
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
        return Webhook(**result)

    async def delete_webhook(self):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}",
        )

    async def execute_webhook(
            self,
            message: ExecuteWebhookReq,
            wait: None | bool = None,
            thread_id: None | ThreadID = None,
    ) -> None | Message:
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

        return Message(**result)

    async def read_webhook_message(self, message_id: MessageID) -> Message:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}/messages/{message_id}",
        )

        return Message(**result)

    async def update_webhook_message(
            self,
            message_id: MessageID,
            message: UpdateWebhookMessageReq,
            thread_id: None | ThreadID = None,
    ) -> Message:
        params = {}

        if thread_id is not None:
            params["thread_id"] = thread_id

        result = await self._request(
            method=Method.PATCH,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}/messages/{message_id}",
            payload=message.dict_as_valid_json(),
            params=params,
        )

        return Message(**result)

    async def delete_webhook_message(
            self,
            message_id: MessageID,
            thread_id: None | ThreadID = None,
    ):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{self.webhook_id}/{self.token}/messages/{message_id}",
        )


class InteractionResponseAPI(InteractionResponseABC):
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

    async def create(self, interaction_id: InteractionID):
        return await self._request(
            method=Method.POST,
            endpoint=f"/interactions/{interaction_id}/{self.token}/callback",
        )

    async def read(self, application_id: ApplicationID) -> Message:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{application_id}/{self.token}/messages/@original",
        )

        return Message(**result)

    async def update(
            self,
            application_id: ApplicationID,
            message: UpdateWebhookMessageReq,
            thread_id: None | ThreadID = None,
    ) -> Message:
        params = {}

        if thread_id is not None:
            params["thread_id"] = thread_id

        result = await self._request(
            method=Method.PATCH,
            endpoint=f"/webhooks/{application_id}/{self.token}/messages/@original",
            payload=message.dict(),
            params=params,
        )

        return Message(**result)

    async def delete(self, application_id: ApplicationID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/interactions/{application_id}/{self.token}/@original",
        )

    async def create_followup(
            self,
            application_id: ApplicationID,
            message: CreateFollowupReq,
    ) -> Message:
        result = await self._request(
            method=Method.POST,
            endpoint=f"/webhooks/{application_id}/{self.token}",
            payload=message.dict(),
        )

        return Message(**result)

    async def read_followup(
            self,
            application_id: ApplicationID,
            message_id: MessageID,
    ) -> Message:
        result = await self._request(
            method=Method.GET,
            endpoint=f"/webhooks/{application_id}/{self.token}/messages/{message_id}",
        )

        return Message(**result)

    async def update_followup(
            self,
            application_id: ApplicationID,
            message_id: MessageID,
            message: UpdateWebhookMessageReq,
            thread_id: None | ThreadID = None,
    ) -> Message:
        params = {}

        if thread_id is not None:
            params["thread_id"] = thread_id

        result = await self._request(
            method=Method.PATCH,
            endpoint=f"/webhooks/{application_id}/{self.token}/messages/{message_id}",
            payload=message.dict(),
            params=params,
        )

        return Message(**result)

    async def delete_followup(self, application_id: ApplicationID, message_id: MessageID):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/webhooks/{application_id}/{self.token}/messages/{message_id}",
        )
