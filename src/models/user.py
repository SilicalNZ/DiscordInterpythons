from __future__ import annotations

from src.models.model_type import Locale, UserPremiumTypes
from src.models.snowflake import UserID
from src.models.flag import UserFlags
from src.models._shared import _BaseModel


class User(_BaseModel):
    # https://discord.com/developers/docs/resources/user#user-object

    S = tuple["User", ...]

    id: UserID
    username: str
    discriminator: str
    avatar: None | str
    bot: None | bool
    system: None | bool
    mfa_enabled: None | bool
    banner: None | bool
    accent_color: None | bool
    locale: None | Locale
    verified: None | str
    email: None | str
    flags: None | UserFlags
    premium_type: None | UserPremiumTypes
    public_flags: None | UserFlags

    @property
    def accent_colour(self) -> None | bool:
        return self.accent_color

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
