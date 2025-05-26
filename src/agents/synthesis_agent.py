"""Synthesis agent for combining news articles."""

from langchain_core.messages import HumanMessage, AIMessage
from src.agents.base_agent import BaseAgent
from src.workflow.state import NewsState
from config.settings import settings

class SynthesisAgent(BaseAgent):
    """Agent responsible for synthesizing information from multiple articles."""
    
    def execute(self, state: NewsState) -> dict:
        """Synthesize information from multiple articles."""
        articles = state["raw_articles"]
        topic = state["topic"]
        
        # Combine article content
        combined_content = ""
        for article in articles[:settings.MAX_ARTICLES_TO_PROCESS]:
            combined_content += f"Title: {article['title']}\nContent: {article['content']}\n\n"
        
        prompt = f"""Analyze these news articles about "{topic}":

{combined_content[:settings.SYNTHESIS_LIMIT]}

Create a 250-word synthesis covering:
1. Main developments
2. Key facts and figures
3. Important stakeholders

Be factual and objective."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        return {
            "synthesized_content": response.content,
            "current_agent": "reporter",
            "messages": [AIMessage(content="Synthesized news content")]
        }
