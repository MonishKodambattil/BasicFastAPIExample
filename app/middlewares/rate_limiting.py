from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time

class RateLimitingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, rate_limit: int):
        super().__init__(app)
        self.rate_limit = rate_limit
        self.requests = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        if client_ip in self.requests:
            if current_time - self.requests[client_ip] < self.rate_limit:
                return Response("Too Many Requests", status_code=429)
        self.requests[client_ip] = current_time
        response = await call_next(request)
        return response
