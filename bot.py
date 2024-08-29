import os
import random

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context

from dotenv import load_dotenv

# Loading Configs
from functions import ConfigManager
config = ConfigManager('config.yml')

load_dotenv()

# Intents 
intents = discord.Intents.default()
intents.message_content = True

# Main Bot
class Tracker(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix = commands.when_mentioned_or(config.fetch('prefix')),
            intents = intents,
            help_command = None
        )
        self.api_key = os.getenv('APIKEY')
    
    async def load_cogs(self) -> None:
        """
        Load bots modules
        """
        for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/modules"):
            if file.endswith(".py"):
                extension = file[:-3]
                try:
                    await self.load_extension(f"modules.{extension}")
                    print(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    print(f"Failed to load extension {extension}\n{exception}")
                
    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:
        """
        Setup the game status task of the bot.
        """
        choices = config.fetch('status')
        await self.change_presence(activity = discord.Game(random.choice(choices)))
    
    @status_task.before_loop
    async def before_status_task(self) -> None:
        await self.wait_until_ready()
    
    async def setup_hook(self) -> None:
        await self.load_cogs()
        self.status_task.start()
    
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user or message.author.bot:
            return
        await self.process_commands(message)

bot = Tracker()
bot.run(os.getenv("TOKEN"))