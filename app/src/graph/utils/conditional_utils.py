"""
Utility functions for graph conditional edges.
Contains all conditional functions used in graph edge decisions.
"""

from typing import Dict, Any

def needs_web_search(state: Dict[str, Any]) -> bool:
    # print("Checking if web search is needed...")
    """
    Check if the current state requires a web search.
    
    Args:
        state: The current graph state containing messages and other data
        
    Returns:
        bool: True if web search is needed, False otherwise
    """
    return str(state["messages"][-1].content == "need_web_search")
