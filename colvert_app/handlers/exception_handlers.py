from fastapi import Request
from fastapi.responses import JSONResponse
from colvert_app.core.exceptions.custom_exceptions import (
    InvalidTokenException,
    UnauthorizedAccessException
)
import logging

logger = logging.getLogger(__name__)

async def invalid_token_exception_handler(request: Request, exc: InvalidTokenException):
    logger.error(f"Invalid token: {exc.message}")
    return JSONResponse(status_code=401, content={"detail": exc.message})

async def unauthorized_access_exception_handler(request: Request, exc: UnauthorizedAccessException):
    logger.error(f"Unauthorized access: {exc.message}")
    return JSONResponse(status_code=403, content={"detail": exc.message})

async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})
