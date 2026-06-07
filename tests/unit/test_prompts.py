import pytest
from backend.prompts.blog_prompts import BlogPrompts
from backend.prompts.social_prompts import SocialPrompts


class TestPrompts:
    def test_blog_system_prompt(self):
        prompts = BlogPrompts()
        system = prompts.get_system_prompt("listicle")
        assert "listicle" in system

    def test_social_user_prompt(self):
        prompts = SocialPrompts()
        user = prompts.get_user_prompt("instagram", "Test topic", "casual", True)
        assert "Test topic" in user
        assert "hashtags" in user
