# External APIs

## Text Generation APIs

| Provider | Library | Model |
|----------|---------|-------|
| OpenAI | openai | GPT-4 |
| Anthropic | anthropic | Claude 3 |
| Groq | groq | Mixtral 8x7b |
| Cohere | cohere | Command-R |

## Image Generation APIs

| Provider | Library | Service |
|----------|---------|---------|
| OpenAI | openai | DALL-E 3 |
| Stability AI | httpx | Stable Diffusion XL |
| Pexels | httpx | Stock photos |
| Pixabay | httpx | Stock photos |
| Unsplash | httpx | Stock photos |

## Voice Generation APIs

| Provider | Library | Service |
|----------|---------|---------|
| ElevenLabs | elevenlabs | TTS + Voice Cloning |
| Google Cloud | google-cloud-texttospeech | TTS |
| Azure | azure-cognitiveservices-speech | Speech |

## Configuration

All API keys are configured via environment variables in `.env`.
