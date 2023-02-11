from __future__ import annotations


__all__ = (
    "Snowflake",
    "Snowflakes",
    "AttachmentID",
    "GuildID",
    "ChannelID",
    "VoiceRegionID",
    "ThreadID",
    "EmojiID",
    "AFKChannelID",
    "InteractionID",
    "ApplicationID",
    "UserID",
    "MessageID",
    "WebhookID",
    "UserOrMessageID",
    "RoleID",
    "BotID",
    "IntegrationID",
    "UserOrRoleID",
    "StickerID",
    "StickerPackID",
    "ApplicationCommandID",
    "Version",
    "ScheduledEvent",
)


class Snowflake(str):
    pass


Snowflakes = tuple[Snowflake, ...]


class AttachmentID(Snowflake):
    pass


class GuildID(Snowflake):
    pass


class ChannelID(Snowflake):
    pass


class VoiceRegionID(str):
    pass


class ThreadID(ChannelID):
    pass


class EmojiID(Snowflake):
    pass


class AFKChannelID(Snowflake):
    pass


class InteractionID(Snowflake):
    pass


class ApplicationID(Snowflake):
    pass


class UserID(Snowflake):
    S = tuple["UserID", ...]


class MessageID(Snowflake):
    pass


class WebhookID(Snowflake):
    pass


class UserOrMessageID(UserID, MessageID):
    pass


class RoleID(Snowflake):
    S = tuple["RoleID", ...]


class BotID(UserID):
    pass


class IntegrationID(Snowflake):
    pass


class UserOrRoleID(UserID, RoleID):
    pass


class StickerID(Snowflake):
    pass


class StickerPackID(Snowflake):
    pass


class ApplicationCommandID(Snowflake):
    pass


class Version(Snowflake):
    pass


class ScheduledEvent(Snowflake):
    pass
