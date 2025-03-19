import sentry_sdk
import logging
from fastapi import FastAPI, BackgroundTasks, Response, status
from fastapi.logger import logger as fastapi_logger
from src.transaction import Transaction
from src.models import Item, Deposit
from src.settings import Settings

transaction = Transaction()
settings = Settings()

gunicorn_logger = logging.getLogger('gunicorn.error')
app = FastAPI()
logger = logging.getLogger(__name__)

fastapi_logger.handlers = gunicorn_logger.handlers
fastapi_logger.setLevel(gunicorn_logger.level)

@app.get("/settings/")
async def showSettings():
    response = settings.showData()
    return response

@app.post("/sample/v1/{wallet}")
async def scrapForPayments(wallet: str, item:Item):
    response = transaction.process_deposit()
    return response