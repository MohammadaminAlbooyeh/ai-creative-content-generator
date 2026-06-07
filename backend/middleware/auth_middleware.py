from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt, JWTError
from backend.utils.config import settings

security = HTTPBearer(auto_error=False)

PUBLIC_PATHS = {
    "/health",
    "/docs",
    "/openapi.json",
    "/redoc",
    "/api/v1/auth/login",
    "/api/v1/auth/register",
}


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        if path in PUBLIC_PATHS or path.startswith("/api/v1/auth/"):
            return await call_next(request)

        if path.startswith("/api/v1"):
            try:
                credentials: HTTPAuthorizationCredentials = await security(request)
                if not credentials:
                    return JSONResponse(
                        status_code=401,
                        content={"detail": "Authentication required"},
                    )
                payload = jwt.decode(
                    credentials.credentials,
                    settings.SECRET_KEY,
                    algorithms=["HS256"],
                )
                request.state.user_id = payload.get("sub")
                request.state.username = payload.get("username")
            except JWTError:
                return JSONResponse(
                    status_code=401,
                    content={"detail": "Invalid or expired token"},
                )

        return await call_next(request)
