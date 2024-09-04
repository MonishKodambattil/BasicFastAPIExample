from fastapi import FastAPI
from app.api import item_router
from app.db import models
from app.db.session import engine
from app.core.log_config import setup_logging
from contextlib import asynccontextmanager
import logging

from app.middlewares import (
    LoggingMiddleware, RateLimitingMiddleware, ErrorHandlingMiddleware
)


models.Base.metadata.create_all(bind=engine)

setup_logging()
logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup tasks
    logger.info(
        " Starting the FastAPI Application "
    )
    yield
    #shutdown tasks
    logger.info("Shutting down the application Server")


app = FastAPI(lifespan=lifespan,
            swagger_ui_parameters={"syntaxHighlight.theme": "Outline"},
            title="Basic FastAPI Example",
            description="An example FastAPI basic crud API application",
            version="0.0.1")


app.add_middleware(LoggingMiddleware, log_format="Method: {0}, URL: {1}")
app.add_middleware(RateLimitingMiddleware, rate_limit=100)
app.add_middleware(ErrorHandlingMiddleware)

app.include_router(item_router, prefix="/api/v1")

