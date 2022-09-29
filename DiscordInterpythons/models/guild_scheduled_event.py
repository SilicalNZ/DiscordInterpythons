from __future__ import annotations

from datetime import datetime

from DiscordInterpythons.models.snowflake import GuildID, ChannelID, ScheduledEvent, Snowflake
from DiscordInterpythons.models.model_type import PrivacyLevel, GuildScheduledEventStatus, GuildScheduledEventEntityType
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models._shared import _BaseModel


class GuildScheduledEventEntityMetadata(_BaseModel):
    location: None | str


class GuildScheduledEvent(_BaseModel):
    id: ScheduledEvent
    guild_id: GuildID
    channel_id: None | ChannelID
    name: str
    description: None | str
    scheduled_start_time: datetime
    scheduled_end_time: None | scheduled_end_time
    privacy_level: PrivacyLevel
    status: GuildScheduledEventStatus
    entity_type: GuildScheduledEventEntityType
    entity_id: None | Snowflake  # TODO: Don't know what this is for
    entity_metadata: None | GuildScheduledEventEntityMetadata
    creator: None | User
    user_count: None | int
    image: None | str
