from __future__ import annotations

from datetime import datetime

from DiscordInterpythons.models.snowflake import RoleID
from DiscordInterpythons.models.flag import Permissions
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models._shared import _BaseModel


class GuildMember(_BaseModel):
    # https://discord.com/developers/docs/resources/guild#guild-member-object

    S = tuple["GuildMember", ...]

    user: User
    nick: None | str
    avatar: None | str
    roles: tuple[RoleID, ...]
    joined_at: datetime
    premium_since: None | datetime
    deaf: bool
    mute: bool
    pending: None | bool
    permissions: None | Permissions
    communication_disabled_until: None | datetime

    @property
    def role_ids(self) -> tuple[RoleID, ...]:
        return self.roles

    _omit = {
        "user",
        "nick",
        "avatar",
        "premium_since",
        "pending",
        "permissions",
        "communication_disabled_until",
    }


class PartialGuildMember(_BaseModel):
    S = tuple["PartialGuildMember", ...]
