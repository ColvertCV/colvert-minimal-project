import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from colvert_app.core import settings
from colvert_app.routes import example_router
from colvert_app.utils import register_exception_handlers

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------
logging.basicConfig(level=logging.DEBUG if settings.debug else logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("Starting Colvert API service")

# ------------------------------------------------------------------------------
# FastAPI Application Setup
# ------------------------------------------------------------------------------
app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    debug=settings.debug,
    root_path=settings.root_path,
)

# ------------------------------------------------------------------------------
# Middleware Configuration (CORS)
# ------------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_origin_regex=".*",  # Optional: allows dynamic origin matching
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allow_methods,
    allow_headers=settings.cors_allow_headers,
    expose_headers=settings.cors_expose_headers,
    max_age=settings.cors_max_age,
)
logger.debug("CORS middleware configured")

# ------------------------------------------------------------------------------
# Exception Handlers
# ------------------------------------------------------------------------------
register_exception_handlers(app)
logger.debug("Global exception handlers registered")

# ------------------------------------------------------------------------------
# Router Registration
# ------------------------------------------------------------------------------
app.include_router(example_router)
logger.debug("API routes registered")

# ------------------------------------------------------------------------------
# Development Server Entry Point
# ------------------------------------------------------------------------------
def run_server():
    logger.debug("Running development server on http://0.0.0.0:8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run_server()
