from __future__ import annotations

from DiscordInterpythons.models.snowflake import InteractionID, ApplicationID, ChannelID, GuildID
from DiscordInterpythons.models.model_type import InteractionType, Locale, InteractionResponseType, ComponentType
from DiscordInterpythons.models.interaction_data import InteractionData, InteractionDataStructures
from DiscordInterpythons.models.guild_member import GuildMember
from DiscordInterpythons.models.user import User
from DiscordInterpythons.models.message import Message
from DiscordInterpythons.models.embed import Embed
from DiscordInterpythons.models.allowed_mention import AllowedMention
from DiscordInterpythons.models.flag import MessageFlags
from DiscordInterpythons.models.component import ActionRow, Button, SelectMenu, TextInput
from DiscordInterpythons.models.attachment import Attachment
from DiscordInterpythons.models._shared import _BaseModel
from DiscordInterpythons.models.application_command import ApplicationCommandOptionChoice


class InteractionToken(str):
    pass


class InteractionCallbackData(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure

    tts: None | bool = None
    content: None | str = None
    embeds: None | Embed.S = None
    allowed_mentions: None | AllowedMention.S = None
    flags: None | MessageFlags = None
    components: None | ActionRow.S = None
    attachments: None | Attachment.S = None

    # TODO: These should be their own classes
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-autocomplete
    choices: None | tuple[ApplicationCommandOptionChoice, ...] = None

    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-modal
    custom_id: None | str = None
    title: None | str = None

    _omit = {
        "tts",
        "content",
        "embeds",
        "allowed_mentions",
        "flags",
        "components",
        "attachments",
        "choices",
        "custom_id",
        "title",
    }


class InteractionResponse(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-response-object-interaction-response-structure

    type: InteractionResponseType
    data: None | InteractionCallbackData = None

    _omit = {
        "data"
    }


class InteractionResponseHandler:
    @classmethod
    def ignore(cls) -> InteractionResponse:
        return InteractionResponse(
            type=InteractionResponseType.DEFERRED_UPDATE_MESSAGE,
        )

    @classmethod
    def auto_complete(cls, choices: tuple[ApplicationCommandOptionChoice]) -> InteractionResponse:
        if len(choices) == 0:
            return InteractionResponse(
                type=InteractionResponseType.APPLICATION_COMMAND_AUTOCOMPLETE_RESULT,
            )

        return InteractionResponse(
            type=InteractionResponseType.APPLICATION_COMMAND_AUTOCOMPLETE_RESULT,
            data=InteractionCallbackData(
                choices=choices,
            )
        )

    @classmethod
    def reply(cls, content: str, colour: None | int = None) -> InteractionResponse:
        return InteractionResponse(
            type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=InteractionCallbackData(
                embeds=(Embed(
                    description=content,
                    colour=colour,
                ),)
            )
        )

    @classmethod
    def complex_reply(
            cls,
            content: None | str = None,
            embeds: None | Embed.S | Embed = None,
            allowed_mentions: None | AllowedMention.S = None,
            flags: None | MessageFlags = None,
            attachments: None | Attachment.S = None,
            components: None
                        | tuple[tuple[Button, SelectMenu, TextInput, ...], ...]
                        | tuple[Button, SelectMenu, TextInput, ...] = None,
    ) -> InteractionResponse:
        action_rows = ()

        if components:
            if not isinstance(components[0], tuple):
                components = (components,)

            action_rows = tuple(ActionRow(
                type=ComponentType.ACTION_ROW,
                components=action_row
            ) for action_row in components)

        return InteractionResponse(
            type=InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            data=InteractionCallbackData(
                content=content,
                embeds=(embeds,) if isinstance(embeds, Embed) else embeds,
                allowed_mentions=allowed_mentions,
                flags=flags,
                components=action_rows or None,
                attachments=attachments,
            ),
        )

    @classmethod
    def defer(cls) -> InteractionResponse:
        return InteractionResponse(
            type=InteractionResponseType.DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE,
        )

    @classmethod
    def update_message(
            cls,
            content: None | str = None,
            embeds: None | Embed.S | Embed = None,
            allowed_mentions: None | AllowedMention.S = None,
            flags: None | MessageFlags = None,
            attachments: None | Attachment.S = None,
            components: None
                        | tuple[tuple[Button, SelectMenu, TextInput, ...], ...]
                        | tuple[Button, SelectMenu, TextInput, ...] = None,
    ) -> InteractionResponse:
        result = cls.complex_reply(
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            flags=flags,
            attachments=attachments,
            components=components,
        )

        result.type = InteractionResponseType.UPDATE_MESSAGE

        return result


class Interaction(_BaseModel):
    # https://discord.com/developers/docs/interactions/receiving-and-responding#interactions

    id: InteractionID
    application_id: ApplicationID
    type: InteractionType
    data: None | InteractionDataStructures
    guild_id: None | GuildID
    channel_id: None | ChannelID
    member: None | GuildMember
    user: None | User
    token: InteractionToken
    version: int
    message: None | Message
    locale: None | Locale
    guild_locale: None | Locale

    def get_sub_command(self) -> None | InteractionData:
        if self.data is None and not isinstance(self.data, InteractionData):
            return None

        return self.data.get_sub_command()

    _omit = {
        "data",
        "guild_id",
        "channel_id",
        "member",
        "user",
        "message",
        "app_permissions",
        "locale",
        "guild_locale",
    }

    response = InteractionResponseHandler
