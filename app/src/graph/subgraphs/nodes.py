from app.src.common.types import SearchGraphState, CrawlGraphState, ReportGraphState


def search_node(state: SearchGraphState):
    return {"bar": "hi! this is from subgraph node: " + state["bar"]}

def crawl_node(state: CrawlGraphState):
    return {}

def report_node(state: ReportGraphState):
    return {}