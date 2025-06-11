# Text-to-SQL Agent for Anton

A LangGraph-based agent that converts natural language queries into SQL and executes them against a MySQL database.

## Quick Start

1. Set up environment with uv:
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS

# Install dependencies
uv pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```env
MYSQL_USERNAME=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_HOST=your_mysql_host
MYSQL_PORT=your_mysql_port
MYSQL_DATABASE=your_database_name
OPENAI_API_KEY=your_openai_api_key
```

3. Run the agent:
```bash
jupyter notebook
# Navigate to notebooks/base_agent.ipynb
```

## Project Structure

```
anton-text2sql-agent/
├── src/
│   └── __init__.py
├── utils/
│   ├── config.py     # Configuration management
│   └── __init__.py
├── notebooks/
│   └── base_agent.ipynb  # Main agent implementation
├── .env                  # Environment variables
├── requirements.txt      # Project dependencies
└── README.md
```

## Dependencies

- Python 3.12.7+
- MySQL database
- OpenAI API key
- Required packages (see requirements.txt)

## Security

- Keep `.env` out of version control
- Secure your OpenAI API key
- Use appropriate database permissions
