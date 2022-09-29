from __future__ import annotations

from DiscordInterpythons.models.model_type import (
    VerificationLevel,
    MessageNotificationLevel,
    ExplicitContentFilterLevel,
    GuildFeatures,
    MFALevel,
    PremiumTier,
    GuildNSFWLevel,
    Locale,
)
from DiscordInterpythons.models.flag import SystemChannelFlags
from DiscordInterpythons.models.snowflake import VoiceRegionID, ChannelID, GuildID, UserID, EmojiID, ApplicationID
from DiscordInterpythons.models.permission_overwrite import Permissions
from DiscordInterpythons.models.role import Role
from DiscordInterpythons.models.emoji import Emoji
from DiscordInterpythons.models.sticker import Sticker
from DiscordInterpythons.models._shared import _BaseModel


class VoiceRegion(_BaseModel):
    # https://discord.com/developers/docs/resources/voice#voice-region-object-voice-region-structure

    id: VoiceRegionID
    name: str
    optimal: bool
    deprecated: bool
    custom: bool


class WelcomeScreenChannel(_BaseModel):
    # https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-channel-structure

    S = tuple["WelcomeScreenChannel", ...]

    channel_id: ChannelID
    description: str
    emoji_id: None | EmojiID
    emoji_name: None | str


class WelcomeScreen(_BaseModel):
    # https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-structure

    description: None | str
    welcome_channels: WelcomeScreenChannel.S


class Guild(_BaseModel):
    # https://discord.com/developers/docs/resources/guild#guild-object-guild-structure

    S = tuple["Guild", ...]

    id: GuildID
    name: str
    icon: None | str
    icon_hash: None | str
    splash: None | str
    discovery_splash: None | str
    owner: None | bool
    owner_id: UserID
    permissions: None | Permissions
    afk_channel_id: None | ChannelID
    afk_timeout: int
    widget_enabled: None | bool
    widget_channel_id: None | ChannelID
    verification_level: VerificationLevel
    default_message_notifications: MessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: Role.S
    emojis: Emoji.S
    features: GuildFeatures
    mfa_level: MFALevel
    application_id: None | ApplicationID
    system_channel_id: None | ChannelID
    system_channel_flags: SystemChannelFlags
    rules_channel_id: None | ChannelID
    max_presences: None | int
    max_members: None | int
    vanity_url_code: None | str
    description: None | str
    banner: None | str
    premium_tier: PremiumTier
    premium_subscription_count: None | int
    preferred_locale: Locale
    public_updates_channel_id: None | ChannelID
    max_video_channel_users: None | int
    approximate_member_count: None | int
    approximate_presence_count: None | int
    welcome_screen: None | WelcomeScreen
    nsfw_level: GuildNSFWLevel
    stickers: None | Sticker.S
    premium_progress_bar_enabled: bool

    _omit = {
        "icon_hash",
        "owner",
        "permissions",
        "region",
        "widget_enabled",
        "widget_channel_id",
        "max_presences",
        "max_members",
        "premium_subscription_count",
        "max_video_channel_users",
        "approximate_member_count",
        "approximate_presence_count",
        "welcome_screen",
        "stickers",
    }
