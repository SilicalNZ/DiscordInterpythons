from dataclasses import dataclass

import aiohttp
import asyncio

from DiscordInterpythons.handlers.handler import InteractionHandlerClass
from DiscordInterpythons.models.snowflake import (
    ApplicationID, 
    GuildID,
)
from DiscordInterpythons.abcs import application_command as abc
from DiscordInterpythons.utils.http_method import Method


__all__ = (
    "ApplicationCommandAPI",
)


@dataclass
class ApplicationCommandAPI(abc.ApplicationCommandABC):
    token: str
    application_id: ApplicationID
    debug_guild_id: None | GuildID
    local_application_commands: abc.ApplicationCommand.S

    @classmethod
    def from_interaction_handler_class(
            cls,
            token: str,
            application_id: None | ApplicationID,
            debug_guild_id: None | GuildID,
    ):
        return cls(
            token=token,
            application_id=application_id,
            debug_guild_id=debug_guild_id,
            local_application_commands=InteractionHandlerClass.generate_application_commands(),
        )

    @property
    def _base_endpoint(self) -> str:
        if self.debug_guild_id:
            return (
                f"https://discord.com/api/v8/applications/"
                f"{self.application_id}/guilds/"
                f"{self.debug_guild_id}/commands"
            )

        return f"https://discord.com/api/v8/applications/{self.application_id}/commands"

    @property
    def _header_auth(self) -> dict[str, str]:
        return {"Authorization": f"Bot {self.token}"}

    @property
    def _header_content_type(self) -> dict[str, str]:
        return {"Content-Type": "application/json"}

    async def _request(
            self,
            *,
            method: Method,
            endpoint: str = "",
            payload: None | dict | list[dict] = None,
            params: None | dict = None,
            headers: None | dict = None,
            respond: bool = True,
    ) -> dict:
        async with aiohttp.ClientSession(
                headers={**self._header_auth, **(headers if headers else {})},
        ) as session:
            async with session.request(
                    method.value,
                    f"{self._base_endpoint}{endpoint}",
                    json=payload,
                    params=params,
            ) as resp:
                if not (200 <= resp.status <= 299):
                    raise AssertionError(f"Code: {resp.status}, URL: {self._base_endpoint}{endpoint}, Response: {await resp.text()}")
                if respond:
                    return await resp.json()
                return {}

    async def read_applications(self) -> abc.ApplicationCommand.S:
        result = await self._request(
            method=Method.GET,
            headers=self._header_content_type,
        )

        return tuple(abc.ApplicationCommand(**i) for i in result)

    async def delete_application(self, application_command: abc.ApplicationCommand):
        await self._request(
            method=Method.DELETE,
            endpoint=f"/{application_command.id}",
            respond=False
        )

    async def create_or_update_application(self, application_command: abc.ApplicationCommand):
        await self._request(
            method=Method.POST,
            headers=self._header_content_type,
            payload=application_command.dict_as_valid_json(),
        )

    async def initialize(self):
        check_deletion_foreign_application_commands = await self.read_applications()

        foreign_application_commands: tuple[abc.ApplicationCommand, ...] = ()
        for foreign_application_command in check_deletion_foreign_application_commands:
            if self._foreign_application_command_should_be_deleted(foreign_application_command):
                await self.delete_application(foreign_application_command)
                await asyncio.sleep(10)  # Arbitrary... should be something smarter
            else:
                foreign_application_commands = (*foreign_application_commands, foreign_application_command)

        for local_application_command in self.local_application_commands:
            if self._application_command_should_be_upserted(foreign_application_commands, local_application_command):
                await self.create_or_update_application(local_application_command)

    def _foreign_application_command_should_be_deleted(self, application_command: abc.ApplicationCommand) -> bool:
        for local_application_command in self.local_application_commands:
            if local_application_command.name == application_command.name:
                return False
        return True

    def _application_command_should_be_upserted(
            self,
            foreign_application_commands: abc.ApplicationCommand.S,
            application_command: abc.ApplicationCommand,
    ) -> bool:
        for foreign_application_command in foreign_application_commands:
            if foreign_application_command.name != application_command.name:
                continue

            return application_command.is_different(foreign_application_command)
        return True

    async def create_or_update_all_applications(self, application_commands: abc.ApplicationCommand.S):
        await self._request(
            method=Method.PUT,
            headers=self._header_content_type,
            payload=[i.dict_as_valid_json() for i in application_commands],
        )
