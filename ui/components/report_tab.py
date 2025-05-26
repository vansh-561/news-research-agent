"""Report tab component."""

import streamlit as st
from src.utils.helpers import ReportUtils

class ReportTab:
    """Report display tab component."""
    
    @staticmethod
    def render(topic):
        """Render the report tab."""
        if st.session_state.get('research_complete') and st.session_state.get('final_report'):
            st.markdown(st.session_state.final_report)
            
            # Download buttons
            ReportTab._render_download_buttons(topic)
            
        elif not st.session_state.get('research_complete'):
            st.info("👆 Start a news research from the sidebar to see results here")
        else:
            st.warning("No report available. Please try running the research again.")
    
    @staticmethod
    def _render_download_buttons(topic):
        """Render download buttons for different formats."""
        report = st.session_state.final_report
        
        # Markdown download
        report_filename = ReportUtils.generate_filename(topic, "md")
        st.download_button(
            label="📄 Download Report",
            data=report,
            file_name=report_filename,
            mime="text/markdown",
            help="Download the complete news report as a Markdown file"
        )
        
        # Additional download formats
        col1, col2 = st.columns(2)
        
        with col1:
            # Plain text version
            plain_text = ReportUtils.convert_to_plain_text(report)
            st.download_button(
                label="📝 Download as TXT",
                data=plain_text,
                file_name=ReportUtils.generate_filename(topic, "txt"),
                mime="text/plain"
            )
        
        with col2:
            # JSON format
            json_report = ReportUtils.create_json_report(
                topic, 
                report, 
                len(st.session_state.get('news_articles', []))
            )
            st.download_button(
                label="📊 Download as JSON",
                data=json_report,
                file_name=ReportUtils.generate_filename(topic, "json"),
                mime="application/json"
            )
