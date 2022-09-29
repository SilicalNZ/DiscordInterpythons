from __future__ import annotations

from DiscordInterpythons.models.snowflake import AttachmentID
from DiscordInterpythons.models._shared import _BaseModel


class Attachment(_BaseModel):
    # https://discord.com/developers/docs/resources/channel#attachment-object-attachment-structure

    S = tuple["Attachment", ...]

    id: AttachmentID
    filename: str
    description: None | str
    content_type: None | str
    size: int
    url: str
    proxy_url: str
    height: None | int
    width: None | int
    ephemeral: None | bool

    _omit = {
        "description",
        "content_type",
        "height",
        "width",
        "ephemeral",
    }
