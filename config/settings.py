"""Configuration settings for the news research agent."""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings."""
    
    # API Keys
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
    
    # LLM Settings
    LLM_MODEL = "gemini-2.0-flash"
    LLM_TEMPERATURE = 0.2
    LLM_MAX_TOKENS = 600
    
    # Search Settings
    MAX_SEARCH_RESULTS = 3
    MAX_ARTICLES_TO_PROCESS = 4
    CONTENT_LIMIT = 300
    SYNTHESIS_LIMIT = 800
    
    # UI Settings
    PAGE_TITLE = "📰 AI News Research Agent"
    PAGE_ICON = "📰"
    
    @classmethod
    def validate_api_keys(cls):
        """Validate that required API keys are present."""
        missing_keys = []
        if not cls.GOOGLE_API_KEY:
            missing_keys.append("GOOGLE_API_KEY")
        if not cls.TAVILY_API_KEY:
            missing_keys.append("TAVILY_API_KEY")
        return missing_keys

settings = Settings()
