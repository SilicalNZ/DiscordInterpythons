from DiscordInterpythons.models import models
from DiscordInterpythons.handlers import handlers


class CommandHandler(handlers.InteractionHandlerClass):
    def __init__(self, shared_variable: bool):
        self.shared_variable = shared_variable
        super().__init__()

    # ----
    # Basic commands
    # ----

    @handlers.ChatInputHandler()
    async def add(
            self,
            interaction: models.Interaction,
            first_value: int,
            second_value: int,
    ) -> models.InteractionResponse:
        """Adds two numbers together

        :param first_value: The first value you want to add something to
        :param second_value: The value you want to add to the first value
        """
        return interaction.response.reply(
            content=f"{first_value} + {second_value} = {first_value + second_value}"
        )

    @handlers.ChatInputHandler(name="subcommand")
    async def send(
            self,
            interaction: models.Interaction,
            text_to_send: str,
    ):
        """Sends the text into the current channel."""
        await interaction.response.reply(text_to_send)

    # ----
    # Subcommands
    # ----

    # TODO: This is lame, change it
    @handlers.ChatInputHandler()
    async def cool(self, interaction: models.Interaction):
        """Says if a user is cool. In reality this just checks if a subcommand is being invoked."""
        await interaction.response.reply(f"No, {interaction.user.username} is not cool")

    @cool.sub_command()
    async def bot(self, interaction: models.Interaction):
        """Is the bot cool?"""
        await interaction.response.reply("Yes, the bot is cool")

    # ----
    # Auto Complete
    # ----

    @handlers.AutoCompleteHandler()
    async def _auto_complete_platform(
            self,
            interaction: models.Interaction,
            options: dict[str, models.InteractionDataOption],
            value: str,
    ) -> models.InteractionResponse:
        return interaction.response.auto_complete(
            (
                models.ApplicationCommandOptionChoice(
                    name="Slack",
                    value="Slack",
                ),
                models.ApplicationCommandOptionChoice(
                    name="Discord",
                    value="Discord",
                ),
            )
        )

    @handlers.ChatInputHandler(
        auto_completes={
            "platform": _auto_complete_platform,
        },
    )
    async def platform(self, interaction: models.Interaction, platform: str):
        """Which platform are you on?"""
        if platform == "Discord":
            return interaction.response.reply("Yes, you are on Discord")
        elif platform == "Slack":
            return interaction.response.reply("No, you are not on Slack")
        else:
            return interaction.response.reply(f"I have never heard of {platform}")

    # ----
    # Buttons
    # ----

    @handlers.ButtonHandler(
        custom_id="1",
    )
    async def button_press(
            self,
            interaction: models.Interaction,
            custom_id: str,
    ) -> models.InteractionResponse:
        return interaction.response.reply(f"Here's a secret for pressing the button: {custom_id}")

    @handlers.ChatInputHandler()
    async def button(self, interaction: models.Interaction):
        """Press a button and receive a secret"""
        return interaction.response.complex_reply(
            content="Press the button!",
            components=(
                self.button_press.build(
                    f"Fish have teeth",
                    "👍",
                ),
            ),
        )
