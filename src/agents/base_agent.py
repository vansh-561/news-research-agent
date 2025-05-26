"""Base agent class for news research agents."""

from abc import ABC, abstractmethod
from src.workflow.state import NewsState

class BaseAgent(ABC):
    """Abstract base class for all agents."""
    
    def __init__(self, llm):
        """Initialize the agent with an LLM."""
        self.llm = llm
    
    @abstractmethod
    def execute(self, state: NewsState) -> dict:
        """Execute the agent's main functionality."""
        pass
