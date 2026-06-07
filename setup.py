from setuptools import setup, find_packages

setup(
    name="ai-creative-content-generator",
    version="0.1.0",
    description="A multi-modal AI content generation platform",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "sqlalchemy>=2.0.0",
        "httpx>=0.25.0",
        "python-dotenv>=1.0.0",
    ],
)
