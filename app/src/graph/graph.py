from langgraph.graph.state import StateGraph, START
from app.src.common.types import State
from app.src.graph.nodes import invoke_search_graph


class MainGraph:
    graph = None
    def __init__(self):
        self.graph_builder = StateGraph(State)
        
        self.graph_builder.add_node("search_node", invoke_search_graph)
        self.graph_builder.add_edge(START, "search_node")
    
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
        
        initial_state = {"foo": query}
        return self.graph.invoke(initial_state)

