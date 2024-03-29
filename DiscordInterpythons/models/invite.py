from __future__ import annotations

from datetime import datetime

from DiscordInterpythons.utils.base import BaseModel
from DiscordInterpythons.models.snowflake import GuildID, ChannelID, RoleID
from DiscordInterpythons.models.model_type import (
    GuildFeatures,
    VerificationLevel,
    GuildNSFWLevel,
    ChannelType,
    InviteTargetType,
)
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.guild_scheduled_event import GuildScheduledEvent


__all__ = (
    "InvitePartialGuild",
    "InvitePartialChannel",
    "InvitePartialMember",
    "InviteStageInstance",
    "Invite",
)


class InvitePartialGuild(BaseModel):
    # https://discord.com/developers/docs/resources/invite#invite-object-example-invite-object

    id: GuildID
    name: str
    splash: None | str
    banner: None | str
    description: str
    icon: None | str
    features: GuildFeatures
    verification_level: VerificationLevel
    vanity_url_code: None | str
    nsfw_level: GuildNSFWLevel
    premium_subscription_count: None | int


class InvitePartialChannel(BaseModel):
    # https://discord.com/developers/docs/resources/invite#invite-object-example-invite-object

    id: ChannelID
    name: str
    type: ChannelType


class InvitePartialMember(BaseModel):
    # https://discord.com/developers/docs/resources/invite#invite-stage-instance-object-example-invite-stage-instance

    S = tuple["InvitePartialMember", ...]

    roles: tuple[RoleID, ...]
    nick: None | str
    avatar: None | str
    premium_since: None | datetime
    joined_at: datetime
    pending: None | bool
    user: User

    @property
    def role_ids(self) -> tuple[RoleID, ...]:
        return self.roles


class InviteStageInstance(BaseModel):
    # https://discord.com/developers/docs/resources/invite#invite-stage-instance-object-invite-stage-instance-structure

    members: InvitePartialMember.S
    participant_count: int
    speaker_count: int
    topic: str


class Invite(BaseModel):
    # https://discord.com/developers/docs/resources/invite#invite-object-invite-structure

    S = tuple["Invite", ...]

    code: str
    guild: None | InvitePartialGuild
    channel: InvitePartialChannel
    inviter: None | User
    target_type: None | InviteTargetType
    target_user: None | User
    target_application: None | dict # TODO: No idea
    approximate_presence_count: None | int
    approximate_member_count: None | int
    expires_at: None | datetime
    stage_instance: None | InviteStageInstance
    guild_scheduled_event: None | GuildScheduledEvent
