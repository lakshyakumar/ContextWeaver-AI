from app.src.common.types import SearchGraphState, CrawlGraphState, ReportGraphState
from langchain_core.messages import  AIMessage



def search_node(state: SearchGraphState):
    return {"messages": [AIMessage(content="searching web for you ..... ")]}

def crawl_node(state: CrawlGraphState):
    return {}

def report_node(state: ReportGraphState):
    return {}