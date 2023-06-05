from typing import Type
from pydantic import BaseModel, Field

from superagi.helper.discord_helper import DiscordHelper
from superagi.tools.base_tool import BaseTool


class DiscordSendMessageInput(BaseModel):
    channel_id: str = Field(..., description="ID of the Discord channel to send the message to")
    message: str = Field(..., description="The message to send")


class DiscordSendMessageTool(BaseTool):
    name: str = "Discord Send Message"
    description: str = "Send a message to a specific Discord channel"
    args_schema: Type[BaseModel] = DiscordSendMessageInput

    def _execute(self, channel_id: str, message: str) -> str:
        discord_helper = DiscordHelper()
        discord_helper.send_message(channel_id, message)
        return "Message sent successfully"
