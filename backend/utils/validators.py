import re

def validate_email(email: str) -> str | None:
    if not email or not email.strip():
        return "Email is required"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email.strip()):
        return "Invalid email format"
    return None

def validate_password(password: str) -> str | None:
    if not password:
        return "Password is required"
    if len(password) < 8:
        return "Password must be at least 8 characters"
    return None

def validate_prompt(prompt: str) -> str | None:
    if not prompt or not prompt.strip():
        return "Prompt is required"
    if len(prompt.strip()) < 3:
        return "Prompt must be at least 3 characters"
    if len(prompt) > 5000:
        return "Prompt must be less than 5000 characters"
    return None

def sanitize_html(text: str) -> str:
    if not text:
        return ""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&#x27;")
    return text

def validate_content_type(content_type: str) -> str | None:
    valid_types = {"blog", "social", "email", "image", "voice", "video", "bundle"}
    if content_type not in valid_types:
        return f"Invalid content type. Must be one of: {', '.join(sorted(valid_types))}"
    return None

def validate_username(username: str) -> str | None:
    if not username or not username.strip():
        return "Username is required"
    if len(username.strip()) < 3:
        return "Username must be at least 3 characters"
    if len(username) > 50:
        return "Username must be less than 50 characters"
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return "Username can only contain letters, numbers, and underscores"
    return None
