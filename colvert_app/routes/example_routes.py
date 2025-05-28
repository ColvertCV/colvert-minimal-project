"""Example routes for the API."""

from fastapi import APIRouter

# Create router
router = APIRouter(tags=["Example"])

@router.get("/example")
async def example_endpoint():
    """
    Example endpoint that returns a simple message.
    
    Returns:
        JSON response with a hello message
    """
    return {"message": "Hello from the example endpoint!"}