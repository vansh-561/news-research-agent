"""Sidebar component for the news research agent."""

import streamlit as st
from src.utils.helpers import UIHelpers

class Sidebar:
    """Sidebar component for user input and controls."""
    
    @staticmethod
    def render():
        """Render the sidebar."""
        with st.sidebar:
            st.header("📰 News Research")
            
            user_topic = st.text_input(
                "Enter news topic:", 
                placeholder="e.g., AI developments, climate change"
            )
            
            start_button = st.button(
                "🔍 Research News", 
                type="primary", 
                disabled=not user_topic
            )
            
            st.divider()
            st.subheader("Example Topics")
            
            examples = UIHelpers.get_example_topics()
            selected_example = None
            
            for example in examples:
                if st.button(example, key=f"ex_{example}"):
                    selected_example = example
            
            st.divider()
            st.info("💡 **Required API Keys:**\n- GOOGLE_API_KEY\n- TAVILY_API_KEY")
            
            return user_topic, start_button, selected_example
