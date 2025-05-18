from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
load_dotenv()

from app.src.router.health import router as health_router
from app.src.router.project_details import router as project_details_router
from app.src.router.crawl import router as crawl_router


app = FastAPI()

# Health API
app.include_router(health_router, prefix="/health", tags=["health"])

app.include_router(project_details_router, tags=["project-details"])

app.include_router(crawl_router, prefix="/query", tags=["query"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)