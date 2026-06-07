from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.middleware.base import BaseHTTPMiddleware

security = HTTPBearer(auto_error=False)


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/api/v1"):
            credentials: HTTPAuthorizationCredentials = await security(request)
            if not credentials:
                raise HTTPException(status_code=401, detail="Authentication required")
        response = await call_next(request)
        return response
