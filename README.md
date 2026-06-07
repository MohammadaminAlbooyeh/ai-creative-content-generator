# AI Creative Content Generator

A production-ready, multi-modal content generation platform powered by multiple LLMs (GPT-4, Claude, Cohere, Groq), image generators (DALL-E, Stability AI), and voice synthesis (ElevenLabs, Google TTS).

## Features

- **Text Generation**: Blog posts, social media, emails, product descriptions, marketing copy, stories, poetry, scripts, technical docs, headlines
- **Image Generation**: DALL-E integration, style transfer, variations
- **Voice Generation**: Text-to-speech, voice cloning, accent/emotion selection
- **Video Generation**: Scripts, thumbnails, subtitles, descriptions
- **Multi-modal Bundles**: Blog with images, social media packs, presentations
- **20+ Pre-built Templates**: Listicles, how-tos, tutorials, reviews, newsletters, and more
- **Prompt Management**: System prompts, optimized templates per content type
- **External API Integration**: OpenAI, Anthropic, Cohere, Groq, ElevenLabs, Google Cloud, Stability AI, stock image services

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Python |
| LLMs | GPT-4, Claude, Cohere, Groq |
| Image | DALL-E, Stability AI |
| Voice | ElevenLabs, Google TTS |
| Frontend | React, Redux |
| Database | PostgreSQL |
| Cache | Redis |
| Storage | AWS S3, Local |
| Testing | Pytest |
| Deployment | Docker |
| Monitoring | Prometheus, Grafana |

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-creative-content-generator.git
cd ai-creative-content-generator

# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Run with Docker
docker-compose up -d

# Or run locally
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Project Structure

```
├── backend/         # FastAPI application
├── frontend/        # React application
├── notebooks/       # Jupyter notebooks
├── examples/        # Usage examples
├── tests/           # Unit, integration, load tests
├── scripts/         # Utility scripts
├── data/            # Raw/processed data
├── docs/            # Documentation
├── config/          # Configuration files
└── monitoring/      # Prometheus/Grafana configs
```

## API Endpoints

- `POST /api/v1/content/generate` - Generate content
- `POST /api/v1/generate/blog` - Blog generation
- `POST /api/v1/generate/social` - Social media generation
- `POST /api/v1/generate/image` - Image generation
- `POST /api/v1/generate/voice` - Voice generation
- `POST /api/v1/generate/video` - Video content
- `POST /api/v1/generate/bundle` - Multi-modal bundles

## License

MIT
