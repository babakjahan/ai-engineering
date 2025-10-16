# AI Engineering Copilot Instructions

## Project Overview
This is an AI engineering learning repository focused on OpenAI API integration and experimentation. The main working directory is `associate_ai_engineer/open_ai_api/` which contains Python scripts demonstrating various OpenAI API usage patterns.

## Environment & Dependencies

### Python Version & Package Management
- **Python 3.13** is specified in `.python-version` 
- Uses **uv** for fast dependency management (preferred over pip)
- Virtual environment pattern: `uv venv` creates `.venv/` in project root

### Environment Setup Workflow
```bash
cd associate_ai_engineer/open_ai_api
uv venv                           # Create .venv folder
source .venv/bin/activate         # Activate on macOS/Linux  
which python                      # Verify environment
```

### Key Dependencies
- `openai>=2.3.0` - Primary OpenAI API client
- `python-dotenv>=1.1.1` - Environment variable management

## Configuration Patterns

### API Key Management
- **Always** use `.env` file for `OPENAI_API_KEY` (gitignored)
- Import pattern: `from config import OPENAI_API_KEY` (see `config.py`)
- Never hardcode API keys in source files

### Config Module Pattern
The `config.py` module centralizes environment loading:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file once
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

## Code Patterns & Conventions

### OpenAI Client Initialization
Standard pattern across all scripts:
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### Chat Completions Structure
- **Model**: Default to `gpt-4o-mini` for cost efficiency
- **Token Limits**: Use `max_completion_tokens` parameter (typically 100-150)
- **Message Format**: Always use proper role structure (`system`, `assistant`, `user`)

### Cost Calculation Pattern
Reference `5-calc_cost.py` for token pricing calculations:
- Input tokens: `$0.15 / 1M tokens`
- Output tokens: `$0.6 / 1M tokens`
- Extract usage: `response.usage.prompt_tokens`

## File Naming & Organization

### Script Naming Convention
- Numbered files (`1-simple_prompt.py`, `5-calc_cost.py`) indicate learning progression
- Descriptive names for standalone examples (`simple_prompt.py`, `prompt_roles.py`)
- Config and utilities in dedicated modules (`config.py`)

### Learning Progression Structure
Files appear to be teaching examples with intentional gaps (incomplete code with `____` placeholders) - when editing, complete these learning exercises rather than starting from scratch.

## Common Issues & Solutions

### Import Errors
- Some files have incorrect imports (`from open_ai_api import OpenAI` should be `from openai import OpenAI`)
- Check for missing `from openai import OpenAI` imports

### Incomplete Code Patterns
- Look for `____` placeholders indicating learning exercises
- Complete missing response extraction: `response.choices[0].message.content`
- Verify role strings are properly quoted (`"assistant"` not `assistant`)

## Development Workflow
1. Always activate the virtual environment first
2. Use `config.py` for centralized environment management
3. Test API calls with minimal token limits during development
4. Calculate costs for any substantial API usage
5. Keep API keys in `.env` and never commit them

## Testing & Validation
- The `test/` directory exists but is currently empty
- Manual testing workflow: run scripts directly with `python script_name.py`
- Verify API responses and token usage before scaling up requests