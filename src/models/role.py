from __future__ import annotations

from src.models.snowflake import BotID, IntegrationID, RoleID
from src.models.flag import Permissions
from src.models._shared import _BaseModel


class RoleTag(_BaseModel):
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


class Role(_BaseModel):
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
