import os
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional

from app.src.models.chat_model import ChatModel


class ChatDatabaseHandler:
    def __init__(self, db_name: str = "chat_database"):
        self.client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
        self.db = self.client[db_name]
        self.collection = self.db["chats"]

    def create_chat(self) -> ObjectId:
        chat = ChatModel(summary="", sentiment="Neutral")  # Create a ChatModel object with empty fields
        self.collection.insert_one(chat.to_dict())  # Insert the object into the database
        return chat.chat_id  # Return the generated 

    def get_chat_by_id(self, chat_id: str) -> Optional[ChatModel]:
        try:
            chat_data = self.collection.find_one({"_id": ObjectId(chat_id)})
            if chat_data:
                return ChatModel(
                    chat_id=chat_data["_id"],
                    summary=chat_data["summary"],
                    sentiment=chat_data["sentiment"]
                )
            return None
        except Exception as e:
            print(f"Error fetching chat: {e}")
            return None

    def update_chat(self, chat_id: str, summary: Optional[str] = None, sentiment: Optional[str] = None) -> bool:
        try:
            update_fields = {}
            if summary:
                update_fields["summary"] = summary
            if sentiment:
                update_fields["sentiment"] = sentiment

            result = self.collection.update_one({"_id": ObjectId(chat_id)}, {"$set": update_fields})
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating chat: {e}")
            return False