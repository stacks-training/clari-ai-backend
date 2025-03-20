from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    APP_NAME = ''

    class Config:
        env_file = ".env"

    # OpenRouter settings
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
    OPENROUTER_BASE_URL: str = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    APP_HOST: str = os.getenv("APP_HOST", "https://your-app-domain.com")

    def showData(self):
        response = {
            'APP_NAME': self.APP_NAME,
        }
        return response
