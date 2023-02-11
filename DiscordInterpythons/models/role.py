from __future__ import annotations

from DiscordInterpythons.models.snowflake import BotID, IntegrationID, RoleID
from DiscordInterpythons.models.flag import Permissions
from DiscordInterpythons.utils.base import BaseModel


__all__ = (
    "RoleTag",
    "Role",
)


class RoleTag(BaseModel):
    # https://discord.com/developers/docs/topics/permissions#role-object-role-tags-structure

    S = tuple["RoleTag", ...]

    bot_id: None | BotID
    integration_id: None | IntegrationID
    premium_subscriber: None | ellipsis  # thankyou danny

    @property
    def is_premium_subscriber(self) -> bool:
        return self.premium_subscriber is None

    _omit = {
        "bot_id",
        "integration_id",
        "premium_subscriber",
    }


class Role(BaseModel):
    # https://discord.com/developers/docs/topics/permissions#role-object-role-structure

    S = tuple["Role", ...]

    id: RoleID
    name: str
    color: int
    hoist: bool
    position: int
    permissions: Permissions
    managed: bool
    mentionable: bool
    icon: None | str
    unicode_emoji: None | str
    tags: None | RoleTag.S

    @property
    def colour(self) -> int:
        return self.color

    _omit = {
        "icon",
        "unicode_emoji",
        "tags",
    }
