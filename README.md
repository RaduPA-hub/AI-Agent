# AI Coding Agent

A command-line AI coding agent written in Python that can inspect, modify, and execute code inside a controlled local workspace.

The agent connects to an LLM through the OpenRouter API using the OpenAI Python SDK. Instead of only generating text, it can choose and execute structured tools, inspect their results, and continue working iteratively until it produces a final response.

## Features

- Interactive command-line interface
- LLM-driven tool/function calling
- Lists files and directories with size and type information
- Reads file contents
- Writes and overwrites files
- Executes Python scripts with optional arguments
- Restricts tool operations to a configured working directory
- Limits file reads to 10,000 characters
- Limits agent execution to 5 iterations
- Optional verbose mode with tool-call and token-usage information
- 30-second timeout for Python script execution

## How It Works

The CLI receives a user prompt and sends it to an LLM together with the available tool definitions.

When the model requests a tool call, the application:

1. Parses the requested function and arguments.
2. Injects the permitted working directory.
3. Dispatches the request to the corresponding Python function.
4. Returns the tool result to the model.
5. Repeats the process until the model produces a final answer or the iteration limit is reached.

The current implementation exposes four tools:

| Tool | Purpose |
| --- | --- |
| `get_files_info` | List files and directories in the workspace |
| `get_file_content` | Read the contents of a file |
| `write_file` | Write or overwrite a file |
| `run_python_file` | Execute a Python script with optional arguments |

## Project Structure

```text
AI-Agent/
├── calculator/              # Sample workspace used by the agent
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── call_function.py         # Tool registry and function dispatcher
├── config.py                # Runtime limits
├── main.py                  # CLI and agent loop
├── prompts.py               # System prompt
├── pyproject.toml
├── .python-version
└── README.md
```

## Requirements

- Python 3.13+
- An OpenRouter API key

The project currently depends on:

- `openai==2.44.0`
- `python-dotenv==1.1.0`

## Installation

Clone the repository:

```bash
git clone https://github.com/RaduPA-hub/AI-Agent.git
cd AI-Agent
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install .
```

## Configuration

Create a `.env` file in the project root and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Do not commit your API key. The repository's `.gitignore` should be used to keep local environment files out of version control.

## Usage

Run the agent by passing a request as a positional argument:

```bash
python main.py "Inspect the calculator project and explain how it works"
```

To display tool calls and token usage, enable verbose mode:

```bash
python main.py --verbose "Run the tests and fix any problems you find"
```

The agent can combine multiple tool calls during a single task. For example, it can inspect the workspace, read relevant source files, modify code, execute a Python file, and use the execution result in its next reasoning step.

## Workspace Safety

Tool calls are currently restricted to the `./calculator` working directory. Each filesystem tool normalizes and validates requested paths before operating on them, preventing the agent from intentionally accessing paths outside the permitted workspace.

Python execution is also restricted to files within this workspace and has a 30-second timeout.

> **Note:** This is an educational/development project. Executing model-selected code can still carry risk. Use it only with code and files you trust, preferably in an isolated environment.

## Current Limitations

- The working directory is currently fixed to `./calculator`.
- The agent supports Python execution only.
- File writes overwrite existing content rather than applying patches.
- The maximum number of agent iterations is currently fixed at 5.
- The model is currently configured as `openrouter/free`.

## Possible Next Steps

- Configurable project/workspace paths
- Patch-based file editing
- Additional development tools
- Improved execution isolation
- Automated tests for tool and path-validation behavior
- More detailed logging and error handling
- Configurable models and runtime limits

## Tech Stack

**Python · OpenAI Python SDK · OpenRouter API · LLM Tool Calling · CLI · subprocess**

## Author

**Radu Antoniu Pătrașcu**

GitHub: [RaduPA-hub](https://github.com/RaduPA-hub)
