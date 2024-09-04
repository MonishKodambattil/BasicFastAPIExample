from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, log_format: str):
        super().__init__(app)
        self.log_format = log_format

    async def dispatch(self, request: Request, call_next):
        print(self.log_format.format(request.method, request.client.host, request.url))
        response = await call_next(request)
        return response
