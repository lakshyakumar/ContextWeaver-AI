# ContextWeaver AI

## Project Description

ContextWeaver AI is a FastAPI-based project designed to build a context-based AI agent leveraging **LangGraph** and **PydanticAI**. The agent is capable of searching the web for information and answering queries based on the gathered data. It incorporates advanced features such as token budgeting, maintaining conversation context, and dynamic decision-making across subgraphs.

### Key Features

1. **Detailed Reporting**: Provides a comprehensive report on any topic by searching the web.
2. **Knowledge Base Creation**: Creates a knowledge base from shared URLs using an efficient chunking strategy.
3. **Context Preservation**: Maintains the context of each conversation for seamless interactions.
4. **QA Agent Integration**: Uses a QA agent in each graph to validate answers and loops the process if the QA agent is not satisfied for each subgraph.
5. **Dynamic Subgraph Switching**: Dynamically decides which subgraph to activate based on the query and context.
6. **Dockerized**: The application is containerized using Docker for easy deployment and scalability.
7. **streamlit frontend chatbot**: Provides a user-friendly interface for interaction with the bot.

## How to Run the Project

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.8 or higher
- `pip` (Python package manager)

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd subgraph-web-bot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venvScriptsactivate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy the `env.sample` file to `.env`:
     ```bash
     cp env.sample .env
     ```
   - Update the `.env` file with your API keys and configuration.

### Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```

### Example Usage

- Use the `query` endpoint to perform a web crawl and get detailed reports.
- Use the `project-details` endpoint to get project metadata.
- Use the `health` endpoint to check the application's health.

## Future Enhancements

- Improved token budgeting strategies.
- Enhanced subgraph decision-making algorithms.
- Support for additional AI models and APIs.

## 🤝 Contributing

We welcome contributions from everyone! Please read our [**Contributing Guide**](CONTRIBUTING.md) to get started. ✨

## License

This project is licensed under the MIT License.