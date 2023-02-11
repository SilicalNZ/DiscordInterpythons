from __future__ import annotations

from DiscordInterpythons.models.emoji import PartialEmoji
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "Reaction",
)


class Reaction(BaseModel):
    # https://discord.com/developers/docs/resources/channel#reaction-object-reaction-structure

    S = tuple["Reaction", ...]

    count: int
    me: bool
    emoji: PartialEmoji
