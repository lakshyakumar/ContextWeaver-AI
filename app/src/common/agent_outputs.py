
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
    
@dataclass
class SearchAgentOutput:
    """
    object to be used in the search agent 
    """
    search_urls: Union[list[str], None] = None
    search_results: Union[str, None] = None
    search_query: Union[str, None] = None
    require_crawling: bool = False
    search_result_markdown: Union[str, None] = None