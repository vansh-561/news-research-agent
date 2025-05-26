"""Search tools for news research."""

from langchain_community.tools import TavilySearchResults
from config.settings import settings

class SearchTools:
    """Wrapper for search tools."""
    
    @staticmethod
    def get_tavily_search():
        """Get configured Tavily search tool."""
        return TavilySearchResults(
            max_results=settings.MAX_SEARCH_RESULTS,
            include_answer=True,
            include_raw_content=False,
            include_images=False,
            search_depth="basic"
        )
