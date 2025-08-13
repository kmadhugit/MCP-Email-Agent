# MCP Email Agent

This project is an AI email agent built with Python, designed to interact with the MCP API and OpenAI services. It reads the email and acts on the email autonomously like calling creating alert for package delivery, scheduling meeting etc.. It helps to understand how to implement a basic AI agent using OpenAI, how to use tool calling features of OpenAI and sample implementation of MCP servers. 

## Features


- Uses OpenAI API for AI-powered features
- Implements with MCP API (`mcp`)
- OpenAI tool calling functionality
- Basic flow of an AI Agent.

## Requirements

See [`requirements.txt`](requirements.txt) for all dependencies:
- `openai`
- `mcp`
- `python-dotenv`
- `requests`
- `flask`

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/<your-username>/<repo-name>.git
   cd MCP\ Email\ Agent
   ```

2. **Create a virtual environment (recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Create a `.env` file in the project root and add your secrets (API keys, etc).

## Usage

Run the Flask server:
```sh
python app.py
```
*(Replace `app.py` with your main Python file if different.)*

## Development

- All Python cache files, logs, virtual environments, and VS Code settings are ignored via `.gitignore`.
- Compatible with macOS and VS Code.

## License

Apache 2.0

