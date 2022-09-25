from __future__ import annotations

from src.models.emoji import PartialEmoji
from src.models._shared import _BaseModel


class Reaction(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#reaction-object-reaction-structure

    S = tuple["Reaction", ...]

    count: int
    me: bool
    emoji: PartialEmoji

