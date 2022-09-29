from __future__ import annotations

from DiscordInterpythons.models.snowflake import EmojiID, RoleID
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models._shared import _BaseModel


class PartialEmoji(_BaseModel):
    S = tuple["PartialEmoji", ...]

    id: EmojiID
    name: str
    animated: bool


class Emoji(_BaseModel):
    # https://discord.com/developers/docs/resources/emoji#emoji-object-emoji-structure

    S = tuple["Emoji", ...]

    id: None | EmojiID
    name: None | str
    roles: tuple[RoleID, ...]
    user: None | User
    require_colons: None | bool
    managed: None | bool
    animated: None | bool
    available: None | bool

    _omit = {
        "roles",
        "user",
        "require_colons",
        "managed",
        "animated",
        "available",
    }
