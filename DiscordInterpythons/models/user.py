from __future__ import annotations

from DiscordInterpythons.models.model_type import Locale, UserPremiumTypes
from DiscordInterpythons.models.snowflake import UserID
from DiscordInterpythons.models.flag import UserFlags
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "User",
)


class User(BaseModel):
    # https://discord.com/developers/docs/resources/user#user-object

    S = tuple["User", ...]

    id: UserID
    username: str
    discriminator: str
    avatar: None | str
    bot: None | bool
    system: None | bool
    mfa_enabled: None | bool
    banner: None | str
    accent_color: None | bool
    locale: None | Locale
    verified: None | str
    email: None | str
    flags: None | UserFlags
    premium_type: None | UserPremiumTypes
    public_flags: None | UserFlags

    _omit = {
        "bot",
        "system",
        "mfa_enabled",
        "banner",
        "accent_color",
        "locale",
        "verified",
        "email",
        "flags",
        "premium_type",
        "public_flags",
    }
