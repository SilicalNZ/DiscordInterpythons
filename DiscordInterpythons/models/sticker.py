from __future__ import annotations

from DiscordInterpythons.models.model_type import StickerFormatType, StickerType
from DiscordInterpythons.models.snowflake import StickerID, GuildID, StickerPackID
from DiscordInterpythons.models.user import User
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "PartialSticker",
    "Sticker",
)


class PartialSticker(BaseModel):
    # https://discord.com/developers/docs/resources/sticker#sticker-item-object-sticker-item-structure

    S = tuple["PartialSticker", ...]

    id: StickerID
    name: str
    format_type: StickerFormatType


class Sticker(BaseModel):
    # https://discord.com/developers/docs/resources/sticker#sticker-object

    S = tuple["Sticker", ...]

    id: StickerID
    name: str
    tags: str
    type: StickerType
    format_type: StickerFormatType
    description: None | str
    pack_id: None | StickerPackID
    available: None | bool
    guild_id: None | GuildID
    user: None | User
    sort_value: None | int

    _omit = {
        "pack_id",
        "asset",
        "available",
        "guild_id",
        "user",
        "sort_value",
    }
