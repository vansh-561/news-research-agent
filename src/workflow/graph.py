"""Workflow graph for news research."""

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI

from src.workflow.state import NewsState
from src.agents import SearchAgent, SynthesisAgent, ReporterAgent
from src.tools.search_tools import SearchTools
from config.settings import settings

class NewsWorkflow:
    """News research workflow using LangGraph."""
    
    def __init__(self):
        """Initialize the workflow."""
        self.llm = self._initialize_llm()
        self.search_tool = SearchTools.get_tavily_search()
        self.app = self._create_workflow()
    
    def _initialize_llm(self):
        """Initialize the LLM."""
        return ChatGoogleGenerativeAI(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_tokens=settings.LLM_MAX_TOKENS
        )
    
    def _create_workflow(self):
        """Create the workflow graph."""
        # Initialize agents
        search_agent = SearchAgent(self.llm, self.search_tool)
        synthesis_agent = SynthesisAgent(self.llm)
        reporter_agent = ReporterAgent(self.llm)
        
        # Create workflow
        workflow = StateGraph(NewsState)
        
        # Add nodes
        workflow.add_node("search", search_agent.execute)
        workflow.add_node("synthesizer", synthesis_agent.execute)
        workflow.add_node("reporter", reporter_agent.execute)
        
        # Add edges
        workflow.set_entry_point("search")
        workflow.add_edge("search", "synthesizer")
        workflow.add_edge("synthesizer", "reporter")
        workflow.add_edge("reporter", END)
        
        # Compile the graph
        memory = MemorySaver()
        return workflow.compile(checkpointer=memory)
    
    def run(self, topic: str):
        """Run the workflow for a given topic."""
        initial_state = {
            "messages": [],
            "topic": topic,
            "search_queries": [],
            "raw_articles": [],
            "synthesized_content": "",
            "final_report": "",
            "current_agent": "search"
        }
        
        config = {"configurable": {"thread_id": "news_thread"}}
        return self.app.stream(initial_state, config)
