import os
from app.src.common.agent_outputs import SearchAgentOutput
from pydantic_ai import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

api_key = os.getenv("TAVILY_API_KEY")
search_agent = Agent(
      os.getenv("MODEL", "gpt-40-mini"),
      tools=[tavily_search_tool(api_key=api_key)],
      output_type=SearchAgentOutput,
  )


@search_agent.system_prompt
def generate_system_prompt() -> str:
    """
    Dynamically generates a system prompt.
    """
    
    # add a prompt such that the llm reply to with the correct prompt if user is ambiguous
    
    return (
        """
        You are a search assistant. Your task is to search DuckDuckGo for the given query and return the results in the specified format. 
        If the query is ambiguous or too broad, divide it into multiple specific queries to ensure accurate and relevant results. 
        Always prioritize clarity and precision in your responses.

        Return the data in the following format:
        - search_urls: Union[list[str], None] = None (A list of URLs from the search results, or None if no results are found)
        - search_results: Union[str, None] = None (A summary or snippet of the search results, or None if no results are found)
        - search_query: Union[str, None] = None (The original or refined search query used, or None if no query was executed)
        - require_crawling: bool = False (Set to True if further crawling is required to gather detailed information on the topic to create article of answer questions from a website)
        - search_result_markdown: Union[str, None] = None (A formatted Markdown summary of the search results, or 'No results found' if no results are found)

        Additional Instructions:
        - If the user query is ambiguous, ask clarifying questions to refine the search.
        - If the query can be broken into sub-queries, perform multiple searches and aggregate the results.
        - Ensure the results are relevant, concise, and formatted correctly.
        - Avoid returning duplicate URLs or irrelevant information.
        """
    )