import abc
from dataclasses import dataclass

from DiscordInterpythons.models import ApplicationCommand


@dataclass
class DiscordApplicationCommandABC(metaclass=abc.ABCMeta):
    local_application_commands: ApplicationCommand.S

    @abc.abstractmethod
    async def read_applications(self) -> ApplicationCommand.S:
        raise NotImplementedError()

    @abc.abstractmethod
    async def delete_application(self, application: ApplicationCommand):
        raise NotImplementedError()

    @abc.abstractmethod
    async def create_or_update_application(self, application: ApplicationCommand):
        raise NotImplementedError()

    @abc.abstractmethod
    async def initialize(self):
        raise NotImplementedError()
