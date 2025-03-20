from openai import OpenAI
import logging
from src.settings import Settings

logger = logging.getLogger(__name__)
settings = Settings()

class AIService:
    """Service for handling AI model interactions via OpenRouter"""
    
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.base_url = settings.OPENROUTER_BASE_URL
        
    async def query_gemini(self, prompt: str):
        try:
            client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key
            )
            completion = client.chat.completions.create(
                model = "google/gemini-2.0-flash-lite-preview-02-05:free",
                messages=[
                        {
                            "role": "user",
                            "content": f"{prompt}"
                        }
                    ]   
            )
            response = completion.choices[0].message.content
            return response
        except Exception as e:
            logger.error(f"Error querying OpenRouter: {str(e)}")
            raise

    async def query_qwen(self, prompt: str):
        try:
            client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key
            )
            completion = client.chat.completions.create(
                model = "qwen/qwq-32b:free",
                messages=[
                        {
                            "role": "user",
                            "content": f"{prompt}"
                        }
                    ]   
            )
            response = completion.choices[0].message.content
            return response
        except Exception as e:
            logger.error(f"Error querying OpenRouter: {str(e)}")
            raise
