from fastapi import APIRouter
from app.config.config import CONFIG

# Create a router instance
router = APIRouter()

@router.get("/")
def description():
    return {"name": CONFIG["name"], "version": CONFIG["version"], "description": CONFIG["description"],  "success": True}