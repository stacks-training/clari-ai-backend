import logging
from fastapi import HTTPException
from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from src.routers import ai_router
from src.settings import Settings

# Initialize settings
settings = Settings()

# Initialize FastAPI app
app = FastAPI()
logger = logging.getLogger(__name__)

# This endpoint is used only for testing purposes
@app.get("/settings/")
async def showSettings():
    response = settings.showData()
    return response
    
app.include_router(ai_router.router, prefix="/api/ai", tags=["AI"])