from typing import Type, List
from pydantic import BaseModel, Field

from superagi.helper.discord_helper import DiscordHelper
from superagi.tools.base_tool import BaseTool


class DiscordReadMessagesInput(BaseModel):
    channel_id: str = Field(..., description="ID of the Discord channel to read messages from")
    limit: int = Field(10, description="Number of messages to retrieve")


class DiscordReadMessagesTool(BaseTool):
    name: str = "Discord Read Messages"
    description: str = "Read messages from a specific Discord channel"
    args_schema: Type[BaseModel] = DiscordReadMessagesInput

    def _execute(self, channel_id: str, limit: int) -> List[str]:
        discord_helper = DiscordHelper()
        messages = discord_helper.read_messages(channel_id, limit)
        return messages
