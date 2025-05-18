from app.src.graph.graph import MainGraph
from fastapi import APIRouter, Query

# Create a router instance
router = APIRouter()
main_graph = MainGraph()
main_graph.compile()


@router.get("/")
def crawl(
     query: str = Query(..., description="What is your aidiate query?"),
     chat_id: str = Query(None, description="Optional chat ID for the conversation")
):
    result =  main_graph.invoke(query, chat_id)
    
    return {"query": query, "chat_id": chat_id, "result": result, "success": True}