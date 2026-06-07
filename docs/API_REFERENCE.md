# API Reference

## Content Management

- `POST /api/v1/content/generate` - Generate content
- `GET /api/v1/content` - List all content
- `GET /api/v1/content/{id}` - Get content by ID
- `PUT /api/v1/content/{id}` - Update content
- `DELETE /api/v1/content/{id}` - Delete content

## Generators

- `POST /api/v1/generate/blog` - Generate blog post
- `POST /api/v1/generate/social` - Generate social media post
- `POST /api/v1/generate/email` - Generate email
- `POST /api/v1/generate/image` - Generate image
- `POST /api/v1/generate/voice` - Generate voice
- `POST /api/v1/generate/video` - Generate video content
- `POST /api/v1/generate/bundle` - Generate multi-modal bundle

## Templates

- `GET /api/v1/templates` - List templates
- `GET /api/v1/templates/{type}` - Get templates by type

## History

- `GET /api/v1/history` - Get generation history
