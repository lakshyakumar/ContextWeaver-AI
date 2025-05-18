

from app.src.common.dependencies import ChatNodeDependency
from app.src.common.types import Sentiment, GraphState
from app.src.db.chat_db_handler import ChatDatabaseHandler
from app.src.graph.agents.chat_agent import chat_agent
from app.src.graph.subgraphs.search_subgraph import SearchGraph
from langchain_core.messages import  AIMessage, HumanMessage

search_graph = SearchGraph()
search_graph.compile()

def invoke_search_graph(state: GraphState):
    # print("Invoking search graph...")
    search_subgraph_output = search_graph.invoke_search_graph( state["query"])  
    return {"messages": search_subgraph_output["messages"][-1]} 

def init_node(state: GraphState):

    # print("Initializing node...")
    db = ChatDatabaseHandler(db_name="context_weaver_ai")
    chat_id = None
    summary = ""
    sentiment = Sentiment.NEUTRAL
    if state["chat_id"] is not None: 
        print(f"Chat ID: {state["chat_id"]} already exists")
        chat_id = state["chat_id"]
        chat = db.get_chat_by_id(chat_id)
        sentiment = chat.sentiment
        summary = chat.summary
    else:
        chat_id = db.create_chat()
        print(f"Chat ID: {chat_id} created")
        state["chat_id"] = chat_id
        state["summary"] = ""
        state["sentiment"] = Sentiment.NEUTRAL
        
    response = { "db": db , "chat_id": chat_id, "summary": summary , "sentiment": sentiment }
    return response

def chat_node(state: GraphState):
    # print("Chat node...")
    result = chat_agent.run_sync(state["query"], deps=ChatNodeDependency( sentiment=state["sentiment"], summary=state["summary"]))
    # print("summary generated: ", result.output.summary)
    return { "messages": [AIMessage(content=result.output.answer)], "summary": result.output.summary, "sentiment": result.output.sentiment }

def updation_node(state: GraphState):
    # print("Updating node...")
    db = state["db"]
    chat_id = state["chat_id"]
    summary = state["summary"]
    sentiment = state["sentiment"]
    
    if chat_id is not None:
        db.update_chat(chat_id, summary=summary, sentiment=sentiment.value)
        print(f"Chat ID: {chat_id} updated")

