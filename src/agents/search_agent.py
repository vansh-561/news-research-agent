"""Search agent for finding news articles."""

from datetime import datetime
from langchain_core.messages import HumanMessage, AIMessage
from src.agents.base_agent import BaseAgent
from src.workflow.state import NewsState
from src.tools.search_tools import SearchTools
import streamlit as st

class SearchAgent(BaseAgent):
    """Agent responsible for searching news articles."""
    
    def __init__(self, llm, search_tool):
        """Initialize the search agent."""
        super().__init__(llm)
        self.search_tool = search_tool
    
    def execute(self, state: NewsState) -> dict:
        """Search for news articles using Tavily."""
        topic = state["topic"]
        
        # Create focused search queries
        prompt = f"""Create 2 specific news search queries for: "{topic}"
Focus on recent news and different aspects.
Keep each query under 6 words.
Format: one query per line."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        queries = [q.strip() for q in response.content.split('\n') if q.strip()][:2]
        
        # Search for articles
        articles = []
        for query in queries:
            try:
                search_results = self.search_tool.invoke({
                    "query": f"{query} news {datetime.now().strftime('%Y')}"
                })
                
                if search_results and isinstance(search_results, list):
                    for result in search_results[:2]:  # Limit results
                        if isinstance(result, dict):
                            article = {
                                "title": result.get('title', 'No title'),
                                "url": result.get('url', ''),
                                "content": result.get('content', '')[:300],  # Limit content
                                "query": query
                            }
                            articles.append(article)
            except Exception as e:
                st.error(f"Search error for '{query}': {str(e)}")
        
        return {
            "search_queries": queries,
            "raw_articles": articles,
            "current_agent": "synthesizer",
            "messages": [AIMessage(content=f"Found {len(articles)} articles")]
        }
