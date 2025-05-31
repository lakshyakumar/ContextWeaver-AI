from app.src.common.types import SearchGraphState, CrawlGraphState, ReportGraphState
from langchain_core.messages import  AIMessage
from app.src.graph.subgraphs.agents import search_agent



def search_node(state: SearchGraphState):
    results = search_agent.run_sync(state["query"])
    # print(f"Search results: {results.output.search_urls}, required crawling: {results.output.require_crawling}")
    return {"messages": [AIMessage(content=results.output.search_result_markdown or "No results found")],}

def crawl_node(state: CrawlGraphState):
    return {}

def report_node(state: ReportGraphState):
    return {}