from nacl.signing import VerifyKey

from DiscordInterpythons import models
from DiscordInterpythons.handlers import handler


def verify_key(raw_body: bytes, signature: str, timestamp: str, client_public_key: str) -> bool:
    message = timestamp.encode() + raw_body
    try:
        vk = VerifyKey(bytes.fromhex(client_public_key))
        vk.verify(message, bytes.fromhex(signature))
        return True
    except Exception:
        return False


async def handle_interaction(data: dict) -> str:
    interaction = models.Interaction(**data)

    if interaction.type == models.InteractionType.PING:
        return models.InteractionResponse(
            type=models.InteractionResponseType.PONG,
        ).json()

    response = await handler.InteractionHandlerClass.call(interaction)
    return response.json()
