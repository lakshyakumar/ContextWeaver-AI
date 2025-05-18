

from dataclasses import dataclass
from typing import Union
from app.src.common.types import Sentiment


@dataclass
class ChatNodeDependency:
    """
    object to be used in the agent 
    """
    sentiment: Union[str, None]
    summary: Union[Sentiment, None]