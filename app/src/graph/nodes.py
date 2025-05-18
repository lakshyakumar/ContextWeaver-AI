

from app.src.common.types import State
from app.src.graph.subgraphs.search_subgraph import SerachGraph

search_graph = SerachGraph()
search_graph.compile()

def invoke_search_graph(state: State):
    subgraph_output = search_graph.invoke_search_graph( state["foo"])  
    return {"foo": subgraph_output["bar"]} 