from __future__ import annotations

from datetime import datetime

from DiscordInterpythons.utils.base import BaseModel
from DiscordInterpythons.models.model_type import EmbedType


__all__ = (
    "EmbedThumbnail",
    "EmbedVideo",
    "EmbedImage",
    "EmbedFooter",
    "EmbedProvider",
    "EmbedAuthor",
    "EmbedField",
    "Embed",
)


# Tempted to put in a type field
class _ViewableFile(BaseModel):
    url: str
    proxy_url: None | str
    height: None | int
    width: None | int

    _omit = {
        "proxy_url",
        "height",
        "width",
    }

    @property
    def size(self) -> None | tuple[int, int]:
        if isinstance(self.height, int) and isinstance(self.width, int):
            return self.width, self.height

        return None


class EmbedThumbnail(_ViewableFile):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-thumbnail-structure

    pass


class EmbedVideo(_ViewableFile):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-video-structure

    _omit = {
        "url",
        *_ViewableFile._omit,
    }


class EmbedImage(_ViewableFile):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-image-structure

    _omit = {
        "url",
        *_ViewableFile._omit,
    }


class EmbedFooter(BaseModel):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-footer-structure

    text: str
    icon_url: None | str
    proxy_icon_url: None | str

    _omit = {
        "icon_url",
        "proxy_icon_url",
    }


class EmbedProvider(BaseModel):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-provider-structure

    name: str
    url: str

    _omit = {
        "name",
        "url",
    }


class EmbedAuthor(BaseModel):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-author-structure

    name: str
    url: None | str
    icon_url: None | str
    proxy_icon_url: None | str

    _omit = {
        "url",
        "icon_url",
        "proxy_icon_url",
    }


class EmbedField(BaseModel):
    # https://discord.com/developers/docs/resources/channel#embed-object-embed-field-structure

    S = tuple["EmbedField", ...]

    name: str
    value: str
    inline: None | bool

    _omit = {
        "inline",
    }


class Embed(BaseModel):
    # https://discord.com/developers/docs/resources/channel#embed-object

    S = tuple["Embed", ...]

    title: None | str = None
    type: None | EmbedType = None
    description: None | str = None
    url: None | str = None
    timestamp: None | datetime = None
    color: None | int = None
    footer: None | EmbedFooter = None
    image: None | EmbedImage = None
    thumbnail: None | EmbedThumbnail = None
    video: None | EmbedVideo = None
    provider: None | EmbedProvider = None
    author: None | EmbedAuthor = None
    fields: None | EmbedField.S = None

    _omit = {
        "title",
        "type",
        "description",
        "url",
        "timestamp",
        "color",
        "footer",
        "image",
        "thumbnail",
        "video",
        "providers",
        "author",
        "fields",
    }

    @property
    def colour(self) -> None | int:
        return self.color
