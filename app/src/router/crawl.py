from app.src.graph.graph import MainGraph
from fastapi import APIRouter, Query, HTTPException
from bson.errors import InvalidId
from bson.objectid import ObjectId

# Create a router instance
router = APIRouter()
main_graph = MainGraph()
main_graph.compile()


@router.get("/")
def crawl(
     query: str = Query(..., description="What is your aidiate query?"),
     chat_id: str = Query(None, description="Optional chat ID for the conversation")
):
    # Validate chat_id format if provided
    if chat_id is not None:
        try:
            # Attempt to convert to ObjectId to validate format
            ObjectId(chat_id)
        except InvalidId:
            raise HTTPException(
                status_code=400,
                detail="Invalid chat_id format. Must be a valid ObjectId string."
            )
    
    try:
        result = main_graph.invoke(query, chat_id)
        
        # Get the chat_id from the result (could be a new one if chat_id was None)
        response_chat_id = result.get("chat_id", chat_id)
        
        return {
            "query": query,
            "chat_id": response_chat_id,
            "result": result,
            "success": True
        }
    except Exception as e:
        # Log the error for debugging (you may want to use proper logging)
        print(f"Error processing request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request. Please try again without a chat_id or with a valid chat_id."
        )
