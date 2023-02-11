from __future__ import annotations

from DiscordInterpythons.models.model_type import PermissionOverwriteType
from DiscordInterpythons.models.flag import Permissions
from DiscordInterpythons.models.snowflake import UserOrRoleID
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "PermissionOverwrite",
)


class PermissionOverwrite(BaseModel):
    # https://discord.com/developers/docs/resources/channel#overwrite-object-overwrite-structure

    S = tuple["PermissionOverwrite", ...]

    id: UserOrRoleID
    type: PermissionOverwriteType
    allow: Permissions
    deny: Permissions
