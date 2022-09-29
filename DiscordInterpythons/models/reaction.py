from __future__ import annotations

from DiscordInterpythons.models.emoji import PartialEmoji
from DiscordInterpythons.models._shared import _BaseModel


class Reaction(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#reaction-object-reaction-structure

    S = tuple["Reaction", ...]

    count: int
    me: bool
    emoji: PartialEmoji

