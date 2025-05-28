import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from colvert_app.core import settings
from colvert_app.routes import example_router  # Adjust if path differs

# Configure logging
logging.basicConfig(level=logging.DEBUG if settings.debug else logging.INFO)
logger = logging.getLogger(__name__)
logger.debug("Starting Colvert API service")

# Initialize FastAPI app with settings
app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version,
    debug=settings.debug,
    root_path=settings.root_path
)

# Configure CORS
try:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_origin_regex=".*",  # Reflect any origin if needed
        allow_credentials=settings.cors_allow_credentials,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
        expose_headers=settings.cors_expose_headers,
        max_age=settings.cors_max_age,
    )
    logger.debug("CORS middleware configured")
except Exception as e:
    logger.error(f"Failed to configure CORS: {e}")
    raise

# Register routers
try:
    app.include_router(example_router)
    logger.debug("API routes registered")
except Exception as e:
    logger.error(f"Failed to include routers: {e}")
    raise

def run_server():
    import uvicorn
    logger.debug(f"Starting server on port 8000")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    run_server()
