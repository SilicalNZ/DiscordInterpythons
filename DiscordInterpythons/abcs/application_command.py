import abc
from dataclasses import dataclass

from DiscordInterpythons.models import ApplicationCommand


@dataclass
class ApplicationCommandABC(metaclass=abc.ABCMeta):
    local_application_commands: ApplicationCommand.S

    # https://discord.com/developers/docs/interactions/application-commands#get-global-application-command
    @abc.abstractmethod
    async def read_applications(self) -> ApplicationCommand.S:
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/application-commands#delete-global-application-command
    @abc.abstractmethod
    async def delete_application(self, application: ApplicationCommand):
        raise NotImplementedError()

    # https://discord.com/developers/docs/interactions/application-commands#create-global-application-command
    @abc.abstractmethod
    async def create_or_update_application(self, application: ApplicationCommand):
        raise NotImplementedError()

    @abc.abstractmethod
    async def initialize(self):
        raise NotImplementedError()
