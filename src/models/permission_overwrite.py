from __future__ import annotations

from src.models.model_type import PermissionOverwriteType
from src.models.flag import Permissions
from src.models.snowflake import UserOrRoleID
from src.models._shared import _BaseModel


class PermissionOverwrite(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#overwrite-object-overwrite-structure

    S = tuple["PermissionOverwrite", ...]

    id: UserOrRoleID
    type: PermissionOverwriteType
    allow: Permissions
    deny: Permissions
