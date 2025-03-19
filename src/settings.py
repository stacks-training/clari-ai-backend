from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME = ''

    class Config:
        env_file = ".env"

    def showData(self):
        response = {
            'APP_NAME': self.APP_NAME,
        }
        return response
