from bson import ObjectId
from langgraph.graph.state import StateGraph, START
from app.src.common.types import GraphState
from app.src.graph.nodes import init_node, invoke_search_graph, updation_node, chat_node
from langchain_core.messages import  AIMessage, HumanMessage


class MainGraph:
    graph = None
    def __init__(self):
        self.graph_builder = StateGraph(GraphState)
        
        self.graph_builder.add_node("search_node", invoke_search_graph)
        # self.graph_builder.add_edge(START, "search_node")
        
        # Add all the nodes
        self.graph_builder.add_node("init_node", init_node)
        self.graph_builder.add_node("updation_node", updation_node)
        self.graph_builder.add_node("chat_node", chat_node)
        
        self.graph_builder.add_edge(START, "init_node")
        self.graph_builder.add_edge("init_node", "chat_node")
        self.graph_builder.add_conditional_edges(
            "chat_node",
            lambda state: str(state["messages"][-1].content == "need_web_search"),
            {
                "True": "search_node",
                "False": "updation_node"
            }
)        # self.graph_builder.add_edge("chat_node", "updation_node")
        self.graph_builder.add_edge("search_node", "updation_node")
        
    
    def compile(self):
        """
        Compile the graph and return the compiled graph.
        """
        self.graph = self.graph_builder.compile()
        
    def invoke(self, query: str, chat_id: str = None):
        """
        Take a query and create initial parameters for the graph.
        """
        if not self.graph:
            raise ValueError("Graph is not compiled. Call compile() before invoke().")
        
        initial_state = {"messages": [HumanMessage(content=query)], "query": query, "chat_id": chat_id}
        response =  self.graph.invoke(initial_state)
        
        # Convert ObjectId to string if present
        if isinstance(response.get("chat_id"), ObjectId):
            response["chat_id"] = str(response["chat_id"])
        
        return {
            "query": response["query"],
            "response": response["messages"][-1].content,
            "summary": response["summary"],
            "sentiment": response["sentiment"],
            "chat_id": response["chat_id"]
        }

