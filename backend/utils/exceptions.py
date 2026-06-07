class BaseAppException(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class GenerationError(BaseAppException):
    def __init__(self, message: str = "Content generation failed"):
        super().__init__(message, status_code=500)


class InvalidRequestError(BaseAppException):
    def __init__(self, message: str = "Invalid request"):
        super().__init__(message, status_code=400)


class NotFoundError(BaseAppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, status_code=404)


class APIKeyError(BaseAppException):
    def __init__(self, message: str = "API key not configured"):
        super().__init__(message, status_code=503)


class RateLimitError(BaseAppException):
    def __init__(self, message: str = "Rate limit exceeded"):
        super().__init__(message, status_code=429)
