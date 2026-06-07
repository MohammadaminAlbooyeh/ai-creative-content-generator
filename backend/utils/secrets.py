import os
from pathlib import Path
from dotenv import load_dotenv

SECRETS_PATH = Path(__file__).resolve().parent.parent.parent / ".env.secrets"
ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"

def load_secrets():
    load_dotenv(dotenv_path=ENV_PATH, override=False)
    load_dotenv(dotenv_path=SECRETS_PATH, override=True)

load_secrets()

def get_secret(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)
