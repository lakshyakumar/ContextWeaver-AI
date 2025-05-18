
from dataclasses import dataclass
from typing import Union

from app.src.common.types import Sentiment


@dataclass
class ChatAgentOutput:
    """
    object to be used in the chat agent 
    """
    summary: Union[str, None]
    sentiment: Union[Sentiment, None]
    answer: str