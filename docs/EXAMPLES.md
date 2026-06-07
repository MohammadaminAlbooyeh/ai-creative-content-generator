# Usage Examples

## Generating a Blog Post

```python
from backend.llm.llm_factory import LLMFactory
from backend.generators.text_generators.blog_post_generator import BlogPostGenerator

factory = LLMFactory()
generator = BlogPostGenerator(factory)
result = await generator.generate("AI in Healthcare", template="listicle")
```

## Generating Social Media Content

```python
from backend.llm.llm_factory import LLMFactory
from backend.generators.text_generators.social_media_generator import SocialMediaGenerator

factory = LLMFactory()
generator = SocialMediaGenerator(factory)
result = await generator.generate("instagram", "Morning routine tips")
```

## Generating Images

```python
from backend.external_apis.openai_client import OpenAIClient
from backend.generators.image_generators.dall_e_generator import DallEGenerator

client = OpenAIClient()
generator = DallEGenerator(client)
images = await generator.generate("A futuristic city")
```
