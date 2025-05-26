"""Helper utilities for the news research agent."""

import json
from datetime import datetime

class ReportUtils:
    """Utilities for report generation and formatting."""
    
    @staticmethod
    def generate_filename(topic: str, extension: str = "md") -> str:
        """Generate a filename for the report."""
        safe_topic = topic.replace(' ', '_').replace('/', '_')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        return f"news_report_{safe_topic}_{timestamp}.{extension}"
    
    @staticmethod
    def convert_to_plain_text(markdown_content: str) -> str:
        """Convert markdown content to plain text."""
        return markdown_content.replace("**", "").replace("*", "")
    
    @staticmethod
    def create_json_report(topic: str, report: str, articles_count: int) -> str:
        """Create a JSON version of the report."""
        report_data = {
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "report": report,
            "articles_count": articles_count
        }
        return json.dumps(report_data, indent=2)

class UIHelpers:
    """UI helper functions."""
    
    @staticmethod
    def get_example_topics() -> list:
        """Get example topics for the sidebar."""
        return [
            "AI breakthrough 2024",
            "Climate summit updates",
            "Tech industry news",
            "Space exploration",
            "Economic trends"
        ]
