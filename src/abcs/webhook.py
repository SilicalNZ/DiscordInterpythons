from __future__ import annotations

from dataclasses import dataclass
import abc

from src import models
from src.models._shared import _BaseModel


class ExecuteWebhookReq(_BaseModel):
    content: str
    username: None | str = None
    avatar_url: None | str = None
    tts: None | bool = None
    embeds: None | models.Embed.S = None
    allowed_mentions: None | models.AllowedMention = None
    components: None | models.Components = None
    # files
    payload_json: str
    attachments: None | models.Attachment.S = None
    flags: None | models.Permissions = None
    thread_name: None | str = None

    _omit = {
        "username",
        "avatar_url",
        "tts",
        "embeds",
        "allowed_mentions",
        "components",
        "payload_json",
        "attachments",
        "flags",
        "thread_name",
    }


class UpdateWebhookMessageReq(_BaseModel):
    content: None | str
    embeds: None | models.Embed.S = None
    allowed_mentions: None | models.AllowedMention = None
    components: None | models.Components = None
    # files
    payload_json: str
    attachments: None | models.Attachment.S = None

    _omit = {
        "content",
        "embeds",
        "allowed_mentions",
        "components",
        "payload_json",
        "attachments",
    }


@dataclass
class WebhookAuthABC(metaclass=abc.ABCMeta):
    # https://discord.com/developers/docs/resources/webhook#create-webhook
    @abc.abstractmethod
    async def create_webhook(
            self,
            channel_id: models.ChannelID,
            name: str,
            avatar: None | str = None,
    ) -> models.Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-channel-webhooks
    @abc.abstractmethod
    async def read_channel_webhooks(self, channel_id: models.ChannelID) -> models.Webhook.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-guild-webhooks
    @abc.abstractmethod
    async def read_guild_webhooks(self, guild_id: models.GuildID) -> models.Webhook.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-webhook
    @abc.abstractmethod
    async def read_webhook(self, webhook_id: models.WebhookID) -> models.Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#modify-webhook
    @abc.abstractmethod
    async def update_webhook(
            self,
            webhook_id: models.WebhookID,
            name: None | str = None,
            avatar: None | str = None,
            channel_id: None | models.ChannelID = None,
    ) -> models.Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#delete-webhook
    @abc.abstractmethod
    async def delete_webhook(self, webhook_id: models.WebhookID) -> models.Webhook:
        raise NotImplementedError()


class DiscordToken(str):
    pass


@dataclass
class WebhookABC(metaclass=abc.ABCMeta):
    webhook_id: models.WebhookID
    token: DiscordToken

    # https://discord.com/developers/docs/resources/webhook#get-webhook-with-token
    @abc.abstractmethod
    async def read_webhook(self) -> models.Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#modify-webhook-with-token
    @abc.abstractmethod
    async def update_webhook_with_token(
            self,
            name: None | str = None,
            avatar: None | str = None,
    ) -> models.Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#delete-webhook-with-token
    @abc.abstractmethod
    async def delete_webhook(self):
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#execute-webhook
    @abc.abstractmethod
    async def execute_webhook(
            self,
            message: ExecuteWebhookReq,
            wait: None | bool = None,
            thread_id: None | models.ThreadID = None,
    ) -> None | models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-webhook-message
    @abc.abstractmethod
    async def read_webhook_message(
            self,
            message_id: models.MessageID,
    ) -> models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#edit-webhook-message
    @abc.abstractmethod
    async def update_webhook_message(
            self,
            message_id: models.MessageID,
            message: UpdateWebhookMessageReq,
            thread_id: None | models.ThreadID = None,
    ) -> models.Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#delete-webhook-message
    @abc.abstractmethod
    async def delete_webhook_message(
            self,
            message_id: models.MessageID,
            thread_id: None | models.ThreadID = None,
    ):
        raise NotImplementedError()
