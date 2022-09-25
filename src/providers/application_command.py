from dataclasses import dataclass

import aiohttp
import asyncio
import json

from src.abcs import models as discord_model
from src.abcs import application_command as abcs


class DiscordToken(str):
    pass


@dataclass
class DiscordApplicationCommandAPI(abcs.DiscordApplicationCommandABC):
    token: DiscordToken
    application_id: discord_model.ApplicationID
    debug_guild_id: None | discord_model.GuildID
    local_application_commands: abcs.ApplicationCommand.S

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

    async def read_applications(self) -> abcs.ApplicationCommand.S:
        url = self._base_endpoint

        async with aiohttp.ClientSession(
                raise_for_status=True,
                headers={
                    **self._header_auth,
                    **self._header_content_type
                }) as session:
            async with session.get(url) as resp:
                result = await resp.json()
                return abcs.ApplicationCommand.cast_from_array(result)

    async def delete_application(self, application: abcs.ApplicationCommand):
        url = f"{self._base_endpoint}/{application.id}"

        async with aiohttp.ClientSession(raise_for_status=True, headers={**self._header_auth}) as session:
            async with session.delete(url):
                pass

    async def create_or_update_application(self, application: abcs.ApplicationCommand):
        url = self._base_endpoint

        async with aiohttp.ClientSession(headers={**self._header_auth, **self._header_content_type}) as session:
            async with session.post(url, data=json.dumps(application.to_dict())):
                pass

    async def initialize(self):
        check_deletion_foreign_application_commands = await self.get_applications()

        foreign_application_commands: tuple[abcs.ApplicationCommand, ...] = ()
        for foreign_application_command in check_deletion_foreign_application_commands:
            if self._foreign_application_command_should_be_deleted(foreign_application_command):
                await self.delete_application(foreign_application_command)
                await asyncio.sleep(5)
            else:
                foreign_application_commands = (*foreign_application_commands, foreign_application_command)

        for local_application_command in self.local_application_commands:
            for foreign_application_command in foreign_application_commands:
                if local_application_command == foreign_application_command:
                    break
            else:
                await self.create_or_update_application(local_application_command)

    def _foreign_application_command_should_be_deleted(self, application_command: abcs.ApplicationCommand) -> bool:
        for local_application_command in self.local_application_commands:
            if local_application_command.name == application_command.name:
                return True

        return False
