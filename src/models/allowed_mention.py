from __future__ import annotations

from src.models.snowflake import RoleID, UserID
from src.models.model_type import AllowedMentionType
from src.models._shared import _BaseModel


class AllowedMention(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#allowed-mentions-object-allowed-mentions-structure

    S = tuple["AllowedMention", ...]

    parse: AllowedMentionType
    roles: RoleID.S
    users: UserID.S
    replied_user: bool
