"""State management for the news research workflow."""

from typing import TypedDict, List, Annotated
import operator

class NewsState(TypedDict):
    """State structure for the news research workflow."""
    messages: Annotated[List, operator.add]
    topic: str
    search_queries: List[str]
    raw_articles: List[dict]
    synthesized_content: str
    final_report: str
    current_agent: str
