"""Example routes for the API."""

from fastapi import APIRouter
from colvert_models.data.load_worker_data import load_worker_data_to_model

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