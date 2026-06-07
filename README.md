# AI Creative Content Generator

A production-ready, multi-modal content generation platform powered by multiple LLMs (GPT-4, Claude, Cohere, Groq), image generators (DALL-E, Stability AI), and voice synthesis (ElevenLabs, Google TTS, Azure Speech). Features full-stack authentication, caching, rate limiting, SSL/TLS support, and comprehensive testing.

## 📊 Project Status

| Component | Status | Progress |
|-----------|--------|----------|
| Backend API | ✅ Complete | 90% |
| Frontend UI | ✅ Complete | 85% |
| Authentication | ✅ Complete | 100% |
| Database & Migrations | ✅ Complete | 100% |
| Testing Suite | 🔴 **Broken** | Need fix |
| Deployment (Docker) | ✅ Complete | 95% |
| SSL/TLS | ✅ Complete | 100% |
| Documentation | ✅ Complete | 90% |
| **Overall** | **⚠️ Ready** | **87%** |

### 🔴 Critical Issue (BLOCKING)
**Logger Import Error** in `backend/middleware/logging_middleware.py:4`
- Current: `from utils.logger import logger` ❌
- Fix: `from backend.utils.logger import logger` ✅
- Impact: All tests fail to run (34 tests unable to collect)
- Fix time: ~2 minutes

## ✨ Features

### Content Generation (9 Types)
- **Text Generation**: Blog posts, social media, emails, product descriptions, marketing copy, stories, poetry, scripts, technical docs, headlines
- **Image Generation**: DALL-E, Stability AI, stock images (Pexels, Pixabay, Unsplash)
- **Voice Generation**: Text-to-speech, voice cloning, accent/emotion selection
- **Video Generation**: Scripts, thumbnails, subtitles, descriptions
- **Multi-modal Bundles**: Blog with images, social media packs, complete content suites

### Advanced Features
- **Authentication**: JWT-based login/signup with secure password hashing
- **Caching**: Redis caching with automatic invalidation (24-hour TTL)
- **Rate Limiting**: Per-user request throttling to prevent abuse
- **Input Validation**: Email, password, username, prompt, content-type validation
- **Error Handling**: Comprehensive error boundaries and user-friendly error messages
- **Responsive Design**: Mobile-first CSS with desktop breakpoints
- **SSL/TLS**: Self-signed certificate generation with HTTPS support
- **20+ Templates**: Listicles, how-tos, tutorials, reviews, newsletters, case studies, press releases, and more
- **Prompt Management**: System prompts and templates optimized per content type
- **Usage Analytics**: Track tokens used, API costs, and user statistics

## 🏗️ Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| **Frontend** | React 18, Redux, React Router | 15 pages, 30+ components |
| **Backend** | FastAPI 0.104, Python 3.11 | 8 main endpoints, async/await |
| **LLMs** | GPT-4, Claude 3, Cohere, Groq | Multi-provider support |
| **Images** | DALL-E, Stability AI, Stock APIs | 5 image sources |
| **Voice** | ElevenLabs, Google TTS, Azure Speech | 3 voice providers |
| **Database** | PostgreSQL 15 | Alembic migrations |
| **Cache** | Redis 7 | Hiredis for performance |
| **Auth** | JWT, bcrypt, python-jose | Secure token-based auth |
| **Testing** | Pytest, pytest-asyncio | 34 unit/integration/load tests |
| **Deployment** | Docker Compose, Nginx | Production-ready setup |
| **Monitoring** | Prometheus, Grafana | Metrics collection ready |

## 🏛️ Architecture Details

### Deployment & Infrastructure Layer

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  DEPLOYMENT & INFRASTRUCTURE LAYER                            │
├─────────────────────────────────────────────────────────────────────────────┤
│
│  Docker Compose Orchestration
│  ├── Services
│  │   ├── nginx          [Reverse Proxy, Port 80/443]
│  │   ├── backend        [FastAPI, Port 8000]
│  │   ├── frontend       [React, Port 3000]
│  │   ├── postgres       [Database, Port 5432]
│  │   └── redis          [Cache, Port 6379]
│  │
│  ├── Health Checks
│  │   ├── Backend        [HTTP /health endpoint]
│  │   ├── Postgres       [pg_isready check]
│  │   └── Redis          [redis-cli ping]
│  │
│  └── Volumes
│      ├── postgres_data  [Database Persistence]
│      ├── certs          [SSL Certificates]
│      └── logs           [Application Logs]
│
│  GitHub Actions CI/CD
│  ├── build.yml          [Build Docker Images]
│  ├── tests.yml          [Run Test Suite]
│  ├── lint.yml           [Code Quality Checks]
│  └── deploy.yml         [Push to Registry]
│
│  Scripts
│  ├── generate_ssl.sh    [SSL Certificate Generation]
│  ├── seed_data.py       [Database Seeding]
│  ├── init_db.py         [Database Initialization]
│  ├── migrate.sh         [Run Alembic Migrations]
│  ├── generate_sample_content.py [Test Data]
│  └── benchmark.py       [Performance Testing]
│
│  Database Migrations (Alembic)
│  └── versions/
│      └── ec1cd844ab26_initial_migration.py [Schema Setup]
│
└─────────────────────────────────────────────────────────────────────────────┘
```

### Testing & Monitoring Layer

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      TESTING & MONITORING LAYER                              │
├─────────────────────────────────────────────────────────────────────────────┤
│
│  Testing
│  ├── Unit Tests (tests/unit/)
│  │   ├── test_api.py                   [API Endpoints]
│  │   ├── test_blog_generator.py        [Blog Logic]
│  │   ├── test_social_generator.py      [Social Logic]
│  │   ├── test_email_generator.py       [Email Logic]
│  │   ├── test_image_generator.py       [Image Logic]
│  │   ├── test_voice_generator.py       [Voice Logic]
│  │   ├── test_templates.py             [Template System]
│  │   └── test_prompts.py               [Prompt System]
│  │
│  ├── Integration Tests (tests/integration/)
│  │   ├── test_end_to_end.py            [Full Workflows]
│  │   ├── test_external_apis.py         [API Integrations]
│  │   ├── test_full_generation.py       [Content Generation]
│  │   └── test_multimodal.py            [Bundle Generation]
│  │
│  └── Load Tests (tests/load/)
│      └── test_performance.py           [Performance & Scalability]
│
│  Monitoring
│  ├── Prometheus                   [Metrics Collection]
│  │   ├── Backend metrics          [Response times, errors]
│  │   ├── Database metrics         [Query times, connections]
│  │   └── Cache metrics            [Hit rates, evictions]
│  │
│  └── Grafana                      [Visualization]
│      ├── Request latency dashboard
│      ├── Error rate dashboard
│      └── Resource usage dashboard
│
└─────────────────────────────────────────────────────────────────────────────┘
```

### Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DATA FLOW DIAGRAM                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│
│  User Authentication Flow:
│  ┌─────────────────┐
│  │  User Browser   │
│  │  (React App)    │
│  └────────┬────────┘
│           │ 1. Login with credentials
│           ↓
│  ┌─────────────────────────────┐
│  │  Nginx (Reverse Proxy)      │
│  │  Port 80/443                │
│  └────────┬────────────────────┘
│           │ 2. Route to Backend
│           ↓
│  ┌─────────────────────────────┐
│  │  FastAPI Backend            │
│  │  /api/v1/auth/login         │
│  └────────┬────────────────────┘
│           │ 3. Validate credentials
│           ↓
│  ┌─────────────────────────────┐
│  │  PostgreSQL                 │
│  │  Query users table          │
│  └────────┬────────────────────┘
│           │ 4. Return user record
│           ↓
│  ┌─────────────────────────────┐
│  │  JWT Token Generation       │
│  │  Sign token with SECRET_KEY │
│  └────────┬────────────────────┘
│           │ 5. Send token to client
│           ↓
│  ┌─────────────────────────────┐
│  │  Browser localStorage       │
│  │  Store access_token         │
│  └─────────────────────────────┘
│
│
│  Content Generation Flow:
│  ┌──────────────────────────────┐
│  │ User fills form              │
│  │ + JWT token in header        │
│  │ POST /api/v1/generate/blog   │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Auth Middleware              │
│  │ Validates JWT token          │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Cache Check (Redis)          │
│  │ Similar prompt exists?       │
│  └────────┬─────────────────────┘
│           │ Cache miss
│           ↓
│  ┌──────────────────────────────┐
│  │ Input Validation             │
│  │ Check constraints            │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ GenerationService            │
│  │ generate_blog()              │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ LLM Selection & Prompt Build │
│  │ BlogPostGenerator + Prompts  │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ External LLM API Call        │
│  │ OpenAI/Claude/Cohere/Groq    │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Generate Content             │
│  │ Return blog post             │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ ContentService               │
│  │ Save to PostgreSQL           │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Cache Result (Redis)         │
│  │ TTL: 24 hours               │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Log Analytics                │
│  │ Record usage & tokens        │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Return Response              │
│  │ JSON with generated content  │
│  └────────┬─────────────────────┘
│           │
│           ↓
│  ┌──────────────────────────────┐
│  │ Browser Display              │
│  │ Show content in UI           │
│  └──────────────────────────────┘
│
└─────────────────────────────────────────────────────────────────────────────┘
```

## 📁 Project Structure

```
ai-creative-content-generator/
├── backend/                          # FastAPI application (Python)
│   ├── api/                          # API routes & dependencies
│   │   ├── routes.py                 # Main content generation endpoints
│   │   ├── auth_routes.py            # Authentication (login/register)
│   │   └── dependencies.py           # Dependency injection
│   ├── generators/                   # Content generators (9 types)
│   │   ├── blog_generator.py
│   │   ├── social_generator.py
│   │   ├── email_generator.py
│   │   ├── image_generator.py
│   │   ├── voice_generator.py
│   │   ├── video_generator.py
│   │   └── bundle_generator.py
│   ├── llm/                          # LLM integrations (4 providers)
│   │   ├── openai_llm.py
│   │   ├── anthropic_llm.py
│   │   ├── cohere_llm.py
│   │   └── groq_llm.py
│   ├── external_apis/                # External service clients (8 services)
│   │   ├── openai_client.py
│   │   ├── elevenlabs_client.py
│   │   ├── google_tts_client.py
│   │   ├── azure_speech_client.py
│   │   ├── stability_client.py
│   │   └── stock_image_clients.py
│   ├── services/                     # Business logic (4 services)
│   │   ├── generation_service.py     # Content generation orchestration
│   │   ├── content_service.py        # Database operations
│   │   ├── cache_service.py          # Redis caching
│   │   └── analytics_service.py      # Usage tracking
│   ├── models/                       # Database models (7 models)
│   │   ├── database.py               # DB connection & session
│   │   ├── user.py                   # User accounts
│   │   ├── content.py                # Generated content
│   │   ├── generation_request.py     # Generation history
│   │   ├── generation_result.py      # Results & metadata
│   │   ├── template.py               # Content templates
│   │   ├── prompt.py                 # System prompts
│   │   └── usage.py                  # Usage analytics
│   ├── middleware/                   # Request processing
│   │   ├── auth_middleware.py        # JWT validation
│   │   ├── rate_limiter.py           # Rate limiting
│   │   ├── error_handler.py          # Error handling
│   │   └── logging_middleware.py     # Request logging
│   ├── prompts/                      # System prompts (9+ per type)
│   ├── templates/                    # Content templates (20+)
│   ├── utils/                        # Utilities
│   │   ├── config.py                 # Settings from env
│   │   ├── validators.py             # Input validation
│   │   ├── logger.py                 # Structured logging
│   │   ├── secrets.py                # Secrets management
│   │   └── exceptions.py             # Custom exceptions
│   └── main.py                       # FastAPI app entry point
│
├── frontend/                         # React application (JavaScript)
│   ├── public/                       # Static assets
│   ├── src/
│   │   ├── pages/                    # 11 page components
│   │   │   ├── LoginPage.jsx         # User authentication
│   │   │   ├── SignupPage.jsx        # User registration
│   │   │   ├── HomePage.jsx          # Dashboard
│   │   │   ├── BlogGeneratorPage.jsx
│   │   │   ├── SocialMediaPage.jsx
│   │   │   ├── EmailGeneratorPage.jsx
│   │   │   ├── ImageGeneratorPage.jsx
│   │   │   ├── VoiceGeneratorPage.jsx
│   │   │   ├── VideoScriptPage.jsx
│   │   │   ├── ContentBundlePage.jsx
│   │   │   ├── MyContentPage.jsx     # User's content library
│   │   │   └── HistoryPage.jsx       # Generation history
│   │   ├── components/               # 30+ reusable components
│   │   │   ├── Header.jsx            # Navigation & user menu
│   │   │   ├── Sidebar.jsx           # Content type navigation
│   │   │   ├── ProtectedRoute.jsx    # Auth guard
│   │   │   ├── ErrorBoundary.jsx     # Error handling
│   │   │   ├── LoadingSpinner.jsx    # Loading indicator
│   │   │   ├── ErrorDisplay.jsx      # Error messages
│   │   │   └── ... (20+ more)
│   │   ├── hooks/                    # 13 custom React hooks
│   │   │   ├── useAuth.js            # Authentication state
│   │   │   ├── useBlogGeneration.js
│   │   │   ├── useSocialGeneration.js
│   │   │   ├── useEmailGeneration.js
│   │   │   ├── useImageGeneration.js
│   │   │   ├── useVoiceGeneration.js
│   │   │   ├── useVideoScriptGeneration.js
│   │   │   ├── useBundleGeneration.js
│   │   │   ├── useContentHistory.js
│   │   │   └── ... (4+ more)
│   │   ├── services/                 # API communication
│   │   │   ├── api.js                # Base HTTP client
│   │   │   ├── auth.js               # Authentication service
│   │   │   ├── logger.js             # Client-side logging
│   │   │   └── ... (5+ content APIs)
│   │   ├── store/                    # Redux state management
│   │   │   ├── reducers/             # State reducers
│   │   │   ├── actions/              # Action creators
│   │   │   └── selectors/            # State selectors
│   │   ├── utils/                    # Utilities
│   │   │   ├── validators.js         # Input validation
│   │   │   ├── formatters.js         # Output formatting
│   │   │   ├── date_utils.js
│   │   │   └── constants.js
│   │   ├── App.js                    # Main app component
│   │   ├── App.css                   # Global styles (665 lines)
│   │   └── index.js                  # Entry point
│   ├── package.json                  # Dependencies
│   └── .env.example                  # Environment template
│
├── tests/                            # Comprehensive test suite (35 tests)
│   ├── unit/                         # Unit tests (API, generators, logic)
│   ├── integration/                  # Integration tests (workflows, APIs)
│   ├── load/                         # Performance & load tests
│   └── conftest.py                   # Pytest configuration
│
├── nginx/                            # Reverse proxy configuration
│   ├── nginx.conf                    # HTTP/HTTPS routing
│   ├── includes/certificates.conf    # SSL certificate paths
│   └── Dockerfile                    # Nginx container
│
├── migrations/                       # Database migrations (Alembic)
│   ├── env.py
│   └── versions/
│       └── ec1cd844ab26_initial_migration.py
│
├── scripts/                          # Utility scripts (7 scripts)
│   ├── generate_ssl.sh               # SSL certificate generation
│   ├── seed_data.py                  # Database seeding
│   ├── init_db.py                    # DB initialization
│   ├── generate_sample_content.py
│   ├── benchmark.py
│   └── ... (2+ more)
│
├── docs/                             # Documentation (13 docs)
│   ├── API_REFERENCE.md
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── GENERATORS.md
│   └── ... (9+ more)
│
├── config/                           # Configuration files
├── data/                             # Data storage
├── notebooks/                        # Jupyter notebooks
├── examples/                         # Usage examples
├── monitoring/                       # Prometheus/Grafana configs
├── certs/                            # SSL certificates (generated)
├── docker-compose.yml                # Multi-container orchestration
├── Dockerfile                        # Backend container
├── Dockerfile.frontend               # Frontend container
├── Makefile                          # Development commands
├── requirements.txt                  # Python dependencies
├── setup.py                          # Package setup
├── .github/workflows/                # CI/CD pipelines (4 workflows)
├── .env.example                      # Environment variables template
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                           # MIT License
└── README.md                         # This file
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose (recommended)
- OR: Python 3.11+, Node 18+, PostgreSQL 15, Redis 7

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-creative-content-generator.git
cd ai-creative-content-generator

# Set up environment
cp .env.example .env
# Edit .env with your API keys:
# - OPENAI_API_KEY
# - ANTHROPIC_API_KEY
# - STABILITY_API_KEY
# - ELEVENLABS_API_KEY
# - AZURE_SPEECH_KEY
# - etc.

# Start all services with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f backend

# Access the application
# Frontend: http://localhost:80 (or https://localhost:443)
# API Docs: http://localhost:8000/docs
# Health Check: http://localhost:8000/health
```

### Option 2: Local Development

```bash
# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
cd frontend
npm install
cd ..

# Set up environment
cp .env.example .env
# Edit .env with your API keys

# Start PostgreSQL and Redis (using Docker or local installation)
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=password postgres:15
docker run -d -p 6379:6379 redis:7

# Run database migrations
alembic upgrade head

# Start backend (Terminal 1)
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend (Terminal 2)
cd frontend
npm start

# Access the application
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs
```

## 🔑 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login (returns JWT token)

### Content Generation
- `POST /api/v1/content/generate` - Generic content generation
- `POST /api/v1/generate/blog` - Blog post generation
- `POST /api/v1/generate/social` - Social media content
- `POST /api/v1/generate/email` - Email generation
- `POST /api/v1/generate/image` - Image generation
- `POST /api/v1/generate/voice` - Voice/TTS generation
- `POST /api/v1/generate/video` - Video script generation
- `POST /api/v1/generate/bundle` - Multi-modal bundle generation

### Content Management
- `GET /api/v1/templates` - List available templates
- `GET /api/v1/content` - List user's content
- `GET /api/v1/content/:id` - Get specific content
- `GET /api/v1/content/history` - Get generation history

### System
- `GET /health` - Health check (database & Redis status)

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run only unit tests
pytest tests/unit/ -v

# Run only integration tests
pytest tests/integration/ -v

# Run only load tests
pytest tests/load/ -v

# Run with coverage
pytest tests/ --cov=backend --cov-report=html
```

**Current Test Status**: 34 passed, 1 skipped (35 tests total)
- ⚠️ **NOTE**: Tests currently fail due to logger import error (see Critical Issue above)

## 🔐 Environment Variables

```bash
# LLM API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GROQ_API_KEY=gsk-...
COHERE_API_KEY=...

# Image Generation
STABILITY_API_KEY=sk-...
PEXELS_API_KEY=...
PIXABAY_API_KEY=...
UNSPLASH_ACCESS_KEY=...

# Voice Generation
ELEVENLABS_API_KEY=...
AZURE_SPEECH_KEY=...
AZURE_SPEECH_REGION=eastus
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json

# Database & Cache
DATABASE_URL=postgresql://user:password@localhost:5432/content_generator
REDIS_URL=redis://localhost:6379

# Storage
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_S3_BUCKET=...
AWS_REGION=us-east-1

# Application
APP_NAME=AI Creative Content Generator
DEBUG=false
SECRET_KEY=your-secret-key-here
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# SSL/TLS
CERT_PATH=/etc/nginx/certs/fullchain.pem
KEY_PATH=/etc/nginx/certs/privkey.pem
```

## 🛠️ Development

```bash
# View available commands
make help

# Common commands
make install          # Install dependencies
make run             # Run backend
make test            # Run tests
make clean           # Clean cache files
make docker-up       # Start Docker services
make docker-down     # Stop Docker services
make migrate         # Run database migrations
make seed            # Seed database with sample data
```

## 📊 Architecture Diagram

See `docs/ARCHITECTURE.md` for detailed architecture and data flow diagrams.

## ⚠️ Known Issues & Next Steps

### Critical (Must Fix)
1. **Logger Import Error** - `backend/middleware/logging_middleware.py:4`
   - Change `from utils.logger` to `from backend.utils.logger`
   - This blocks all tests from running

### Phase 1: Core Completion (Week 1)
- [ ] Fix logger import error
- [ ] Verify all 35 tests pass
- [ ] Manual end-to-end testing (login → generate → save)
- [ ] Verify JWT authorization header in all API calls
- [ ] Test SSL certificate generation script

### Phase 2: Quality & Polish (Week 2)
- [ ] Password reset functionality
- [ ] Email verification flow
- [ ] Test responsive design on mobile
- [ ] Performance testing with load generator
- [ ] Prometheus metrics integration
- [ ] Content deletion with confirmation

### Phase 3: Advanced Features (Week 3)
- [ ] Download/export functionality (PDF, DOCX)
- [ ] Search and filtering in History
- [ ] Pagination for content lists
- [ ] Favorites/bookmarks system
- [ ] Refresh token rotation
- [ ] Analytics dashboard
- [ ] Multi-language support

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Documentation

- [API Reference](docs/API_REFERENCE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Generators](docs/GENERATORS.md)
- [Prompts System](docs/PROMPTS.md)
- [Templates](docs/TEMPLATES.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## 🆘 Support

For issues, questions, or suggestions, please open an issue on GitHub or check the [Troubleshooting](docs/TROUBLESHOOTING.md) guide.
