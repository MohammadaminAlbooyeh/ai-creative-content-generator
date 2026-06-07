# Quickstart Guide

## Prerequisites

- Python 3.10+
- Node.js 18+
- Docker (optional)

## Installation

1. Clone the repository
2. Copy `.env.example` to `.env` and add your API keys
3. Install Python dependencies: `pip install -r requirements.txt`
4. Install frontend dependencies: `cd frontend && npm install`
5. Start the backend: `uvicorn backend.main:app --reload`
6. Start the frontend: `cd frontend && npm start`

## Your First Generation

Visit `http://localhost:8000/docs` for the API documentation.
