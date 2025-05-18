from enum import Enum
from typing import Union, Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

from app.src.db.chat_db_handler import ChatDatabaseHandler


class Sentiment(Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"

class GraphState(TypedDict):
    query: str
    db: ChatDatabaseHandler
    chat_id: Union[str, None]
    summary: str
    sentiment: Sentiment
    messages: Annotated[list, add_messages]
    
class SearchGraphState(TypedDict):
    query: str
    messages: Annotated[list, add_messages]
    
    
class CrawlGraphState(TypedDict):
    query: str
    
class ReportGraphState(TypedDict):
    query: str
    
    
