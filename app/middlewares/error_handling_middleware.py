from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
        except Exception as e:
            response = Response("Internal Server Error", status_code=500)
            print(f"Error: {str(e)}")
        
        return response
