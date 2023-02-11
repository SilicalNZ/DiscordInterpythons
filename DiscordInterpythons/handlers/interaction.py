from DiscordInterpythons.models.interaction import Interaction, InteractionResponse
from DiscordInterpythons.models.model_type import InteractionResponseType, InteractionType
from DiscordInterpythons.handlers.handler import InteractionHandlerClass


__all__ = (
    "handle_interaction",
)


async def handle_interaction(data: dict) -> dict:
    interaction = Interaction(**data)

    if interaction.type == InteractionType.PING:
        return InteractionResponse(
            type=InteractionResponseType.PONG,
        ).dict_as_valid_json()

    response = await InteractionHandlerClass.call(interaction)
    return response.dict_as_valid_json()
