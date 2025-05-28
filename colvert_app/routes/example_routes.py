"""Example routes for the API."""

import logging
from fastapi import APIRouter
from colvert_models.data.load_worker_data import load_worker_data_to_model
from colvert_i18n import Translator
from fastapi.params import Depends
from colvert_app.core.auth.jwt_bearer import JWTBearer

# Create router
router = APIRouter(tags=["Example"])
logger = logging.getLogger(__name__)

@router.get("/example")
async def example_endpoint():
    """
    Example endpoint that returns a simple message.
    
    Returns:
        JSON response with a hello message
    """
    return {"message": "Hello from the example endpoint!"}

@router.get("/worker/{worker_id}")
async def get_worker_data(worker_id: str):
    """
    Get worker data for a specific worker ID.
    
    Args:
        worker_id: The ID of the worker to fetch
        
    Returns:
        JSON response with the worker data
    """
    worker_instance = load_worker_data_to_model(worker_id)
    if worker_instance:
        return worker_instance.model_dump()
    return {"error": f"Could not load worker data for worker {worker_id}"}

@router.get("/translation-test/{language}")
async def test_translation(language: str = "en"):
    """
    Test endpoint for colvert_i18n translations.
    
    Args:
        language: The language code (e.g. 'en' or 'fr')
        
    Returns:
        JSON response with translations of some test words
    """
    translator = Translator(language=language)
    test_words = ['hello', 'education', 'hard_skills', 'soft_skills']
    
    translations = {}
    for word in test_words:
        translations[word] = translator.gettext(word) if translator.has_translation(word) else f"No translation found for '{word}'"
    
    return {
        "language": language,
        "translations": translations
    }

@router.get('/jwt-validation',dependencies=[Depends(JWTBearer())])
async def test_jwt_validation():
    """
    Test endpoint for JWT validation.
    
    Args:
        authorization: Authorization header (format: "Bearer <token>")
        
    Returns:
        JSON response with validation result
        
    Raises:
        InvalidTokenException: If token is invalid
    """
    return {"message": "JWT validation successful"}