from __future__ import annotations

from DiscordInterpythons.models.snowflake import RoleID, UserID
from DiscordInterpythons.models.model_type import AllowedMentionType
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "AllowedMention",
)


class AllowedMention(BaseModel):
    # https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mentions-structure

    S = tuple["AllowedMention", ...]

    parse: AllowedMentionType
    roles: RoleID.S
    users: UserID.S
    replied_user: bool
