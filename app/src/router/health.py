from fastapi import APIRouter, Query

# Create a router instance
router = APIRouter()

@router.get("/")
def health():
    
    return {"message": "Health check successful!", "success": True}