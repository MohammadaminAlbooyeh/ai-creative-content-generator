# Architecture

## System Design

The application follows a modular architecture:

- **Backend**: FastAPI with service-oriented design
- **LLM Layer**: Abstract factory pattern for multiple LLM providers
- **Generator Layer**: Specialized generators per content type
- **Template Layer**: Reusable content templates
- **Prompt Layer**: Structured prompt management
- **Frontend**: React SPA with Redux state management

## Key Design Patterns

- **Factory Pattern**: LLMFactory for provider-agnostic LLM access
- **Strategy Pattern**: Different generators implement common interface
- **Template Method**: Content templates provide structure
- **Service Layer**: Business logic abstraction
