from enum import Enum


class ApplicationCommandOptionType(Enum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10
    ATTACHMENT = 11

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class ChannelType(Enum):
    # https://discord.com/developers/docs/resources/channel#channel-object-channel-types

    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13
    GUILD_DIRECTORY = 14
    GUILD_FORUM = 15

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


ChannelTypes = tuple[ChannelType, ...]


class ButtonStyleType(Enum):
    Primary = 1
    Secondary = 2
    Success = 3
    Danger = 4
    Link = 5

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class ComponentType(Enum):
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3
    TEXT_INPUT = 4

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class TextInputStyleType(Enum):
    # https://discord.com/developers/docs/interactions/message-components#text-inputs-text-input-styles

    Short = 1
    Paragraph = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class EmbedType(str, Enum):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-types

    RICH = "rich"
    IMAGE = "image"
    VIDEO = "video"
    GIFV = "gifv"
    ARTICLE = "article"
    LINK = "link"

    UNKNOWN = "UNKNOWN"

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class VerificationLevel(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class MessageNotificationLevel(Enum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class ExplicitContentFilterLevel(Enum):
    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class MFALevel(Enum):
    NONE = 0
    ELEVATED = 1

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class GuildNSFWLevel(Enum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class PremiumTier(Enum):
    # https://discord.com/developers/docs/resources/guild#guild-object-premium-tier

    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class GuildFeature(Enum):
    ANIMATED_BANNER = "ANIMATED_BANNER"
    ANIMATED_ICON = "ANIMATED_ICON"
    BANNER = "BANNER"
    COMMERCE = "COMMERCE"
    COMMUNITY = "COMMUNITY"
    DISCOVERABLE = "DISCOVERABLE"
    FEATURABLE = "FEATURABLE"
    INVITE_SPLASH = "INVITE_SPLASH"
    MEMBER_VERIFICATION_GATE_ENABLED = "MEMBER_VERIFICATION_GATE_ENABLED"
    MONETIZATION_ENABLED = "MONETIZATION_ENABLED"
    MORE_STICKERS = "MORE_STICKERS"
    NEWS = "NEWS"
    PARTNERED = "PARTNERED"
    PREVIEW_ENABLED = "PREVIEW_ENABLED"
    PRIVATE_THREADS = "PRIVATE_THREADS"
    ROLE_ICONS = "ROLE_ICONS"
    TICKETED_EVENTS_ENABLED = "TICKETED_EVENTS_ENABLED"
    VANITY_URL = "VANITY_URL"
    VERIFIED = "VERIFIED"
    VIP_REGIONS = "VIP_REGIONS"
    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"

    UNKNOWN = "UNKNOWN"

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


GuildFeatures = tuple[GuildFeature, ...]


class InteractionResponseType(Enum):
    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class InteractionType(Enum):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-type

    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class Locale(str, Enum):
    # https://discord.com/developers/docs/reference#locales

    Danish = "da"
    German = "de"
    EnglishUK = "en-GB"
    EnglishUS = "en-US"
    Spanish = "es-ES"
    French = "fr"
    Croatian = "hr"
    Italian = "it"
    Lithuanian = "lt"
    Hungarian = "hu"
    Dutch = "nl"
    Norwegian = "no"
    Polish = "pl"
    PortugueseBrazilian = "pt-BR"
    RomanianRomania = "ro"
    Finnish = "fi"
    Swedish = "sv-SE"
    Vietnamese = "vi"
    Turkish = "tr"
    Czech = "cs"
    Greek = "el"
    Bulgarian = "bg"
    Russian = "ru"
    Ukrainian = "uk"
    Hindi = "hi"
    Thai = "th"
    ChineseChina = "zh-CN"
    Japanese = "ja"
    ChineseTaiwan = "zh-TW"
    Korean = "ko"

    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class MessageType(Enum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    GUILD_MEMBER_JOIN = 7
    USER_PREMIUM_GUILD_SUBSCRIPTION = 8
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_1 = 9
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_2 = 10
    USER_PREMIUM_GUILD_SUBSCRIPTION_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class MessageActivityType(Enum):
    # https://discord.com/developers/docs/resources/channel#message-object-message-activity-types

    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class PermissionOverwriteType(Enum):
    # https://discord.com/developers/docs/resources/channel#overwrite-object-overwrite-structure

    ROLE = 0
    MEMBER = 1

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class StickerType(Enum):
    # https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-types

    STANDARD = 1
    GUILD = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class StickerFormatType(Enum):
    # https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-format-types

    PNG = 1
    APNG = 2
    LOTTIE = 3

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class UserPremiumTypes(Enum):
    # https://discord.com/developers/docs/resources/user#user-object-premium-types

    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class ApplicationCommandType(Enum):
    # https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types

    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class AllowedMentionType(str, Enum):
    # https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mention-types

    ROLE = "roles"
    USER = "users"
    EVERYONE = "everyone"

    UNKNOWN = "unknown"

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class InviteTargetType(Enum):
    # https://discord.com/developers/docs/resources/invite#invite-object-invite-target-types

    STREAM = 1
    EMBEDDED_APPLICATION = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class PrivacyLevel(Enum):
    # https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-privacy-level

    GUILD_ONLY = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class GuildScheduledEventStatus(Enum):
    # https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-status

    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class GuildScheduledEventEntityType(Enum):
    # https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-types

    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class AutoArchiveDuration(Enum):
    # https://discord.com/developers/docs/resources/channel#start-thread-from-message-json-params

    EEN = 60
    TWEE = 1440
    DRIE = 4320
    VIER = 10080

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class VideoQualityModes(Enum):
    # https://discord.com/developers/docs/resources/channel#channel-object-video-quality-modes

    AUTO = 1
    FULL = 2

    UNKNOWN = 9999

    @classmethod
    def _missing_(cls, value: object):
        return cls(cls.UNKNOWN)


class WebhookType(Enum):
    # https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-types

    Incoming = 1
    ChannelFollower = 2
    Application = 3
