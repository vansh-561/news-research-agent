"""Research tab component."""

import streamlit as st

class ResearchTab:
    """Research process tab component."""
    
    @staticmethod
    def render(workflow, topic):
        """Render the research tab."""
        st.write(f"🔍 **Researching news about:** {topic}")
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Run the workflow
            step = 0
            for state in workflow.run(topic):
                step += 1
                current_state = list(state.values())[0]
                
                # Update progress
                progress = min(step * 33, 100)
                progress_bar.progress(progress)
                
                # Update status
                agent = current_state.get("current_agent", "unknown")
                status_text.write(f"**Current Step:** {agent.title()} Agent")
                
                # Store results in session state
                if current_state.get("raw_articles"):
                    st.session_state.news_articles = current_state["raw_articles"]
                
                if current_state.get("final_report"):
                    st.session_state.final_report = current_state["final_report"]
                    st.session_state.research_complete = True
            
            progress_bar.progress(100)
            status_text.write("✅ **Research Complete!**")
            
        except Exception as e:
            st.error(f"Error during research: {str(e)}")
            st.info("This might be due to API rate limits. Try again in a moment.")
