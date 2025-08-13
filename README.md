# MCP Email Agent

This project is an email agent built with Python, designed to interact with the MCP API and OpenAI services. It uses Flask for web server functionality and manages environment variables securely with `python-dotenv`.

## Features

- Integrates with MCP API (`mcp`)
- Uses OpenAI API for AI-powered features

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

