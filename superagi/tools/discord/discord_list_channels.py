from typing import Type, List
from pydantic import BaseModel

from superagi.helper.discord_helper import DiscordHelper
from superagi.tools.base_tool import BaseTool

class DiscordListChannelsInput(BaseModel):
    guild_id: str = ""


class DiscordListChannelsTool(BaseTool):
    name: str = "Discord List Channels"
    description: str = "List all channels in a Discord guild"
    args_schema: Type[BaseModel] = DiscordListChannelsInput
    
    def _execute(self, guild_id: str) -> List[str]:
        discord_helper = DiscordHelper()
        channels = discord_helper.list_channels(guild_id)
        return channels
