# AI News Research Agent

A sophisticated multi-agent news research system powered by Google Gemini, Tavily Search, and LangGraph that automatically searches, synthesizes, and generates professional news reports.

## 🚀 Features

- **Multi-Agent Architecture**: Specialized agents for search, synthesis, and reporting
- **Real-time News Research**: Automated search across multiple sources using Tavily API
- **Professional Report Generation**: Creates structured news reports in AP/Reuters style
- **Multiple Export Formats**: Download reports as Markdown, TXT, or JSON
- **Interactive UI**: Clean Streamlit interface with real-time progress tracking
- **Modular Design**: Well-organized codebase for easy maintenance and extension

## 🏗️ System Architecture

The system employs three specialized agents working in sequence:

1. **Search Agent**: Finds relevant news articles using optimized search queries
2. **Synthesis Agent**: Analyzes and synthesizes information from multiple sources
3. **Reporter Agent**: Creates professional news reports with proper formatting

## 📋 Prerequisites

- Python 3.13 or higher
- Google Gemini API key
- Tavily Search API key

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/news-research-agent.git
cd news-research-agent
```

2. Create a virtual environment : Install Poetry (if not already installed)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies
```bash
poetry install
```

4. Set up environment variables
```bash
cp .env.example .env
```

Edit the `.env` file and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

![Screenshot (110)](https://github.com/user-attachments/assets/313f88f6-dade-4f0f-941c-18515a4edca5)
![Screenshot (107)](https://github.com/user-attachments/assets/a05745ee-179c-4d68-a302-20c3f0b0a9ee)
![Screenshot (108)](https://github.com/user-attachments/assets/91a53610-cb9a-4ebf-8497-4f4eb63f986d)
![Screenshot (109)](https://github.com/user-attachments/assets/06973873-91b8-4999-adba-0ed1bdabbd0f)

## 🚀 Usage

1. Start the application
```bash
streamlit run main.py
```

2. Access the web interface
   - Open your browser and navigate to http://localhost:8501

3. Research news topics
   - Enter a news topic in the sidebar
   - Click "Research News" to start the multi-agent workflow
   - Monitor the research process in real-time
   - Download the final report in your preferred format

## 🔧 Configuration

The application can be configured through the `config/settings.py` file:

- **LLM Settings**: Model selection, temperature, token limits
- **Search Settings**: Maximum results, content limits
- **UI Settings**: Page title, icons, layout options
