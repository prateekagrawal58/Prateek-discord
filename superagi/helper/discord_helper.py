import discord
from discord.ext import commands
from typing import List

class DiscordHelper:
    def __init__(self):
        self.bot = commands.Bot(command_prefix="!")

    def read_messages(self, channel_id: str, limit: int) -> List[str]:
        @self.bot.event
        async def on_ready():
            channel = self.bot.get_channel(int(channel_id))
            messages = await channel.history(limit=limit).flatten()
            message_content = [msg.content for msg in messages]
            self.bot.close()
            return message_content
        self.bot.run("MTExNTI1MzY1MzE0NjcxMDA2Ng.G0Z2xS.BhzoXQ6aHrIxi-3Yz6hWhzJ3YlHxs9IOSAsj9Y")

    def send_message(self, channel_id: str, message: str):
        @self.bot.event
        async def on_ready():
            channel = self.bot.get_channel(int(channel_id))
            await channel.send(message)
            self.bot.close()
        
        self.bot.run("MTExNTI1MzY1MzE0NjcxMDA2Ng.G0Z2xS.BhzoXQ6aHrIxi-3Yz6hWhzJ3YlHxs9IOSAsj9Y")