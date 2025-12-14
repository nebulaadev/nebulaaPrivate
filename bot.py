import discord
from discord import app_commands
from discord.ext import commands
import os

folderPath = r"Lib\bot"
stopMacroFile = os.path.join(folderPath, "stopMacro.txt")
statusFile = os.path.join(folderPath, "status.txt")
reconnectFile = os.path.join(folderPath, "reconnect.txt")

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name="stopmacro", description="Stops the macro")
async def stopmacro(interaction: discord.Interaction):
    try:
        os.makedirs(folderPath, exist_ok=True)
        with open(stopMacroFile, "w", encoding="utf-8") as f:
            print(1, file=f)

        await interaction.response.send_message(
            "Macro stopped",
            ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(
            f"Error: {e}",
            ephemeral=True
        )

@bot.tree.command(name="status", description="Sends a webhook showing macro status")
async def status(interaction: discord.Interaction):
    try:
        os.makedirs(folderPath, exist_ok=True)
        with open(statusFile, "w", encoding="utf-8") as f:
            print(1, file=f)

        await interaction.response.send_message(
            "Webhook sent",
            ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(
            f"Error: {e}",
            ephemeral=True
        )
        
@bot.tree.command(name="reconnect", description="Forces the macro to reconnect")
async def reconnect(interaction: discord.Interaction):
    try:
        os.makedirs(folderPath, exist_ok=True)
        with open(reconnectFile, "w", encoding="utf-8") as f:
            print(1, file=f)

        await interaction.response.send_message(
            "Macro reconnected",
            ephemeral=True
        )
    except Exception as e:
        await interaction.response.send_message(
            f"Error: {e}",
            ephemeral=True
        )


with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read()

bot.run(token)
