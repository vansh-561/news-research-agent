"""Reporter agent for creating final news reports."""

from langchain_core.messages import HumanMessage, AIMessage
from src.agents.base_agent import BaseAgent
from src.workflow.state import NewsState

class ReporterAgent(BaseAgent):
    """Agent responsible for creating the final news report."""
    
    def execute(self, state: NewsState) -> dict:
        """Create the final news report."""
        topic = state["topic"]
        synthesis = state["synthesized_content"]
        articles = state["raw_articles"]
        
        prompt = f"""Create a professional news report about "{topic}".

Synthesis: {synthesis}

Format as a news report with:
1. Headline
2. Lead paragraph (40 words)
3. Body (150 words)
4. Key points (3 bullet points)

Use AP/Reuters style. Be concise and factual."""
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        
        # Add sources section
        sources = "\n\n**Sources:**\n"
        for i, article in enumerate(articles[:3], 1):
            sources += f"{i}. {article['title']} - {article['url']}\n"
        
        final_report = response.content + sources
        
        return {
            "final_report": final_report,
            "current_agent": "complete",
            "messages": [AIMessage(content="News report completed")]
        }
