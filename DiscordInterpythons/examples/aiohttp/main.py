from typing import Coroutine, Any, Callable

from aiohttp import web
import asyncio
from DiscordInterpythons.models import models
from DiscordInterpythons.providers import providers
from DiscordInterpythons.handlers import handlers


from .command import CommandHandler

# ----
# DISCORD_TOKEN should not be provided here, this is purely for an example
# At minimum provide through .env
# ----
DISCORD_TOKEN = ""

DISCORD_APPLICATION_ID = models.ApplicationID("")
# This is used, so you can test freely, remove for a production environment
DISCORD_DEBUG_GUILD_ID = models.GuildID("")

DISCORD_PUBLIC_KEY = "bd396703929de2af5cc2283a6c58d5a9b6e86a91f83c2ac41f870cc65da3a987"

# Initialize the CommandHandler
_ = CommandHandler(True)


try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# We need to initialize our commands with Discord before we use them.
# This runs through Upsert logic to avoid ratelimiting

discord_application_command_api = providers.ApplicationCommandAPI.from_interaction_handler_class(
    token=DISCORD_TOKEN,
    application_id=DISCORD_APPLICATION_ID,
    debug_guild_id=DISCORD_DEBUG_GUILD_ID,
)

loop.run_until_complete(discord_application_command_api.initialize())


# A verification wrapper

_type_callable_web_request = Callable[
    [web.Request],
    Coroutine[Any, Any, web.Response],
]


def _verify(
        f: _type_callable_web_request
) -> _type_callable_web_request:
    async def _wrapper(request: web.Request) -> web.Response:
        signature = request.headers.get("X-Signature-Ed25519")
        timestamp = request.headers.get("X-Signature-Timestamp")
        if signature is None \
                or timestamp is None \
                or not handlers.verify_key(await request.read(), signature, timestamp, DISCORD_PUBLIC_KEY):
            raise web.HTTPUnauthorized(reason="Bad request signature")
        return await f(request)
    return _wrapper


# The router

@_verify
async def router(request: web.Request) -> web.Response:
    data = await request.json()

    result = await handlers.handle_interaction(data)

    return web.json_response(result)


app = web.Application()

app.router.add_post("/", router)
