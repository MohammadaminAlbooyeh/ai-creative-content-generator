import re


def validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_url(url: str) -> bool:
    pattern = r"^https?://[^\s/$.?#].[^\s]*$"
    return bool(re.match(pattern, url))


def validate_content_length(content: str, min_length: int = 10, max_length: int = 50000) -> tuple[bool, str]:
    if len(content) < min_length:
        return False, f"Content too short (min {min_length} chars)"
    if len(content) > max_length:
        return False, f"Content too long (max {max_length} chars)"
    return True, ""
