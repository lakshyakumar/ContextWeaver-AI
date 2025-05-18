from typing_extensions import TypedDict

class State(TypedDict):
    foo: str
    
class SearchGraphState(TypedDict):
    bar: str
    
    
class CrawlGraphState(TypedDict):
    crawl: str
    
class ReportGraphState(TypedDict):
    report: str