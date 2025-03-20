from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import logging

from models.ai_models import GeminiRequest, GeminiResponse, QwenRequest, QwenResponse
from src.services.ai_service import AIService

logger = logging.getLogger(__name__)
router = APIRouter()


    
@router.post("/gemini", response_model=GeminiResponse)
async def query_gemini(request: GeminiRequest):
    """
    Endpoint for querying Gemini 2.0 Flash model via OpenRouter
    """
    print(request)
    try:
        ai_service = AIService()
        response = await ai_service.query_gemini(
            prompt=request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        return JSONResponse(content=response)
    except Exception as e:
        logger.error(f"Error querying Gemini: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error querying Gemini: {str(e)}")


@router.post("/qwen", response_model=QwenResponse)
async def query_qwen(request: QwenRequest):
    """
    Endpoint for querying Qwen QWQ model
    """
    try:
        ai_service = AIService()
        response = await ai_service.query_qwen(
            prompt=request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        return JSONResponse(content=response)
    except Exception as e:
        logger.error(f"Error querying Qwen: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error querying Qwen: {str(e)}")

@router.get("/test")
async def test_endpoint():
    return {"msg": "AI route working"}