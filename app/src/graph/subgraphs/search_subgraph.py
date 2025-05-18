from langgraph.graph.state import StateGraph, START

from app.src.common.types import SearchGraphState
from app.src.graph.subgraphs.nodes import search_node
from langchain_core.messages import  AIMessage


class SearchGraph:
    search_graph = None
    
    def __init__(self):
        self.search_graph_builder = StateGraph(SearchGraphState)
        self.search_graph_builder.add_node(search_node)
        self.search_graph_builder.add_edge(START, "search_node")
        
    def compile(self):
        """
        Compile the graph and return the compiled graph.
        """
        self.search_graph = self.search_graph_builder.compile()
        
    def invoke_search_graph(self, query):
        """
        Invoke the search graph with the given state.
        """
        if self.search_graph is None:
            self.compile()
        return self.search_graph.invoke({"query": query})
        
        
    

