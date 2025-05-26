"""Main Streamlit application."""

import streamlit as st
from config.settings import settings
from src.workflow.graph import NewsWorkflow
from ui.components.sidebar import Sidebar
from ui.components.research_tab import ResearchTab
from ui.components.report_tab import ReportTab

class NewsResearchApp:
    """Main application class."""
    
    def __init__(self):
        """Initialize the application."""
        self._configure_page()
        self._check_api_keys()
        self._initialize_session_state()
        self.workflow = NewsWorkflow()
    
    def _configure_page(self):
        """Configure Streamlit page."""
        st.set_page_config(
            page_title=settings.PAGE_TITLE,
            page_icon=settings.PAGE_ICON,
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    def _check_api_keys(self):
        """Check for required API keys."""
        missing_keys = settings.validate_api_keys()
        if missing_keys:
            for key in missing_keys:
                st.error(f"Please set your {key} environment variable")
            st.stop()
    
    def _initialize_session_state(self):
        """Initialize session state variables."""
        if "news_articles" not in st.session_state:
            st.session_state.news_articles = []
        if "research_complete" not in st.session_state:
            st.session_state.research_complete = False
        if "final_report" not in st.session_state:
            st.session_state.final_report = None
    
    def run(self):
        """Run the main application."""
        # App title and description
        st.title(settings.PAGE_TITLE)
        st.subheader("Powered by Google Gemini, Tavily Search & LangGraph")
        st.markdown("Multi-agent news research system with downloadable reports")
        
        # Render sidebar
        user_topic, start_button, selected_example = Sidebar.render()
        
        # Handle example selection
        if selected_example:
            user_topic = selected_example
            start_button = True
        
        # Create tabs
        tab1, tab2, tab3 = st.tabs(["🔍 Research Process", "📄 Final Report", "📊 Articles Found"])
        
        # Research execution
        if start_button and user_topic:
            self._reset_session_state()
            
            with tab1:
                ResearchTab.render(self.workflow, user_topic)
        
        # Display final report
        with tab2:
            ReportTab.render(user_topic if 'user_topic' in locals() else "")
        
        # Display found articles
        with tab3:
            self._render_articles_tab()
        
        # Footer
        st.markdown("---")
        st.markdown("Built with 🔍 Google Gemini, 🌐 Tavily Search, 🦜 LangChain, and 📊 Streamlit")
    
    def _reset_session_state(self):
        """Reset session state for new research."""
        st.session_state.news_articles = []
        st.session_state.research_complete = False
        st.session_state.final_report = None
    
    def _render_articles_tab(self):
        """Render the articles tab."""
        if st.session_state.news_articles:
            st.write(f"📊 **Found {len(st.session_state.news_articles)} articles:**")
            
            for i, article in enumerate(st.session_state.news_articles, 1):
                with st.expander(f"Article {i}: {article['title'][:60]}..."):
                    st.write(f"**Title:** {article['title']}")
                    st.write(f"**URL:** {article['url']}")
                    st.write(f"**Search Query:** {article['query']}")
                    st.write(f"**Content Preview:** {article['content'][:200]}...")
        
        elif not st.session_state.research_complete:
            st.info("👆 Start a news research to see found articles here")
        else:
            st.warning("No articles found. Please try a different topic.")
