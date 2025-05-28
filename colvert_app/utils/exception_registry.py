from fastapi import FastAPI
from colvert_app.core.exceptions.custom_exceptions import (
    InvalidTokenException,
    UnauthorizedAccessException
)
from colvert_app.handlers import exception_handlers

def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(InvalidTokenException, exception_handlers.invalid_token_exception_handler)
    app.add_exception_handler(UnauthorizedAccessException, exception_handlers.unauthorized_access_exception_handler)
    app.add_exception_handler(Exception, exception_handlers.generic_exception_handler)
