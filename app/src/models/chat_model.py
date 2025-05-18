from typing import Optional
from bson import ObjectId

class ChatModel:
    def __init__(self, chat_id: Optional[ObjectId] = None, summary: str = "", sentiment: str = ""):
        self.chat_id = chat_id or ObjectId()
        self.summary = summary
        self.sentiment = sentiment

    def to_dict(self):
        return {
            "_id": self.chat_id,
            "summary": self.summary,
            "sentiment": self.sentiment
        }