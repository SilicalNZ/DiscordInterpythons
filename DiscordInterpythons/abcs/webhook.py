from __future__ import annotations

from dataclasses import dataclass
import abc

from DiscordInterpythons.models.snowflake import (
    ChannelID, MessageID, WebhookID, ThreadID, GuildID, InteractionID, ApplicationID
)
from DiscordInterpythons.models.flag import Permissions
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.embed import Embed
from DiscordInterpythons.models.allowed_mention import AllowedMention
from DiscordInterpythons.models.component import ActionRow
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.models.webhook import Webhook
from DiscordInterpythons.models.interaction import InteractionToken
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "WebhookAuthABC",
    "WebhookABC",
    "InteractionResponseABC",
    "ExecuteWebhookReq",
    "UpdateWebhookMessageReq",
    "CreateFollowupReq",
)


class ExecuteWebhookReq(BaseModel):
    content: str
    username: None | str = None
    avatar_url: None | str = None
    tts: None | bool = None
    embeds: None | Embed.S = None
    allowed_mentions: None | AllowedMention = None
    components: None | ActionRow.S = None
    # files
    payload_json: str
    attachments: None | Attachment.S = None
    flags: None | Permissions = None
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


class CreateFollowupReq(BaseModel):
    content: str
    tts: None | bool = None
    embeds: None | Embed.S = None
    allowed_mentions: None | AllowedMention = None
    components: None | ActionRow.S = None
    # files
    payload_json: str
    attachments: None | Attachment.S = None
    flags: None | Permissions = None
    thread_name: None | str = None

    _omit = {
        "tts",
        "embeds",
        "allowed_mentions",
        "components",
        "payload_json",
        "attachments",
        "flags",
        "thread_name",
    }


class UpdateWebhookMessageReq(BaseModel):
    content: None | str
    embeds: None | Embed.S = None
    allowed_mentions: None | AllowedMention = None
    components: None | ActionRow.S = None
    # files
    payload_json: str
    attachments: None | Attachment.S = None

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
            channel_id: ChannelID,
            name: str,
            avatar: None | str = None,
    ) -> Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-channel-webhooks
    @abc.abstractmethod
    async def read_channel_webhooks(self, channel_id: ChannelID) -> Webhook.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-guild-webhooks
    @abc.abstractmethod
    async def read_guild_webhooks(self, guild_id: GuildID) -> Webhook.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-webhook
    @abc.abstractmethod
    async def read_webhook(self, webhook_id: WebhookID) -> Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#modify-webhook
    @abc.abstractmethod
    async def update_webhook(
            self,
            webhook_id: WebhookID,
            name: None | str = None,
            avatar: None | str = None,
            channel_id: None | ChannelID = None,
    ) -> Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#delete-webhook
    @abc.abstractmethod
    async def delete_webhook(self, webhook_id: WebhookID) -> Webhook:
        raise NotImplementedError()


@dataclass
class WebhookABC(metaclass=abc.ABCMeta):
    webhook_id: WebhookID
    token: str

    # https://discord.com/developers/docs/resources/webhook#get-webhook-with-token
    @abc.abstractmethod
    async def read_webhook(self) -> Webhook:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#modify-webhook-with-token
    @abc.abstractmethod
    async def update_webhook_with_token(
            self,
            name: None | str = None,
            avatar: None | str = None,
    ) -> Webhook:
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
            thread_id: None | ThreadID = None,
    ) -> None | Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#get-webhook-message
    @abc.abstractmethod
    async def read_webhook_message(
            self,
            message_id: MessageID,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#edit-webhook-message
    @abc.abstractmethod
    async def update_webhook_message(
            self,
            message_id: MessageID,
            message: UpdateWebhookMessageReq,
            thread_id: None | ThreadID = None,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/resources/webhook#delete-webhook-message
    @abc.abstractmethod
    async def delete_webhook_message(
            self,
            message_id: MessageID,
            thread_id: None | ThreadID = None,
    ):
        raise NotImplementedError()


@dataclass
class InteractionResponseABC(metaclass=abc.ABCMeta):
    token: InteractionToken

    # https://discord.com/developers/docs/interactions/receiving-and-responding#create-interaction-response
    @abc.abstractmethod
    async def create(
            self,
            interaction_id: InteractionID,
    ):
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#get-original-interaction-response
    @abc.abstractmethod
    async def read(
            self,
            application_id: ApplicationID,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#edit-original-interaction-response
    @abc.abstractmethod
    async def update(
            self,
            application_id: ApplicationID,
            message: UpdateWebhookMessageReq,
            thread_id: None | ThreadID = None,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#delete-original-interaction-response
    @abc.abstractmethod
    async def delete(
            self,
            application_id: ApplicationID,
    ):
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#create-followup-message
    @abc.abstractmethod
    async def create_followup(
            self,
            application_id: ApplicationID,
            message: CreateFollowupReq,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#get-followup-message
    @abc.abstractmethod
    async def read_followup(
            self,
            application_id: ApplicationID,
            message_id: MessageID,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#edit-followup-message
    @abc.abstractmethod
    async def update_followup(
            self,
            application_id: ApplicationID,
            message_id: MessageID,
            message: UpdateWebhookMessageReq,
            thread_id: None | ThreadID = None,
    ) -> Message:
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/receiving-and-responding#delete-followup-message
    @abc.abstractmethod
    async def delete_followup(
            self,
            application_id: ApplicationID,
            message_id: MessageID,
    ):
        raise NotImplementedError()
