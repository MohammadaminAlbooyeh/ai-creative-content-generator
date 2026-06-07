import pytest
from backend.templates.blog_templates.listicle_template import ListicleTemplate
from backend.templates.blog_templates.how_to_template import HowToTemplate


class TestTemplates:
    def test_listicle_render(self):
        template = ListicleTemplate()
        items = [
            {"title": "Test List", "intro": "Here are the top items"},
            {"title": "Item 1", "description": "Description 1"},
            {"conclusion": "That's the list"},
        ]
        result = template.render(items)
        assert "Test List" in result
        assert "Item 1" in result

    def test_how_to_render(self):
        template = HowToTemplate()
        result = template.render(
            steps=["Do step 1", "Do step 2"],
            title="How to Test",
            intro="This is how you test",
            supplies=["A computer", "Python"],
        )
        assert "How to Test" in result
        assert "Do step 1" in result
