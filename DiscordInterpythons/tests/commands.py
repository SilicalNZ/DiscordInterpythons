from unittest import TestCase
from enum import Enum

from DiscordInterpythons.handlers.handler import (
    ChatInputHandler, InteractionHandlerClass
)
from DiscordInterpythons.models.interaction import Interaction
from DiscordInterpythons.models.channel import Channel, PartialChannel

class Test(TestCase):
    def test_choices(self):
        class TestEnum(Enum):
            One = 1
            Two = 2


        class CommandHandler(InteractionHandlerClass):
            @ChatInputHandler(name="set_ss_target")
            async def action(self, interaction: Interaction, choice: TestEnum):
                """Change the name that will be displayed for a player

                :param choice: Choose one or two"""
                return interaction.response.reply("OK")

        CommandHandler()

        res = InteractionHandlerClass.generate_application_commands()
        self.assertTrue(len(res[0].options[0].choices) == 2)
