from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app, origins: list[str] = None):
    if origins is None:
        origins = ["http://localhost:3000", "http://localhost:8000"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
