from typing import Optional
from pydantic import BaseModel


class GeminiRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 1024
    temperature: Optional[float] = 0.7

class GeminiResponse(BaseModel):
    response: str
    model: str

class QwenRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 1024
    temperature: Optional[float] = 0.7

class QwenResponse(BaseModel):
    response: str
    model: str