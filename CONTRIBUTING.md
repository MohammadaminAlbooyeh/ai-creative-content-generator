# Contributing

## Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your API keys
6. Run the development server: `uvicorn backend.main:app --reload`

## Code Style

- Follow PEP 8 for Python
- Use ESLint + Prettier for JavaScript/React
- Write docstrings for all public functions
- Add type hints to Python code

## Testing

- Write tests for all new features
- Run `pytest tests/` before submitting
- Ensure all tests pass

## Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure CI passes
4. Get at least one review approval
