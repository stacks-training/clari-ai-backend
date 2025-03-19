from asyncio.base_futures import _PENDING
from request import Request
from src.settings import Settings
import logging
request = Request()
settings = Settings()
logger = logging.getLogger(__name__)
from fastapi.logger import logger as fastapi_logger

class Transaction():
    PENDING_STATUS = 'pending'
    FAILED_STATUS = 'failed'
    SUCCESS_STATUS = 'success'
    MAX_ATTEMPTS = settings.MAX_ATTEMPTS
    MOBILE_MAX_ATTEMPTS = settings.MOBILE_MAX_ATTEMPTS
    ERROR_DEPOSIT_NOT_FOUND = 'Deposit not found'
    ETH_NETWORK = 1

    '''
    Scrap data for mobile
    '''
    async def process_deposit(self, deposit):
        last_txhash = deposit.txhash
        networkId = deposit.networkId
        counter = 0
        is_new_tx = False
        body = {}

        # build initial body
        body['orderCode'] = deposit.orderCode
        body['status'] = self.FAILED_STATUS
        
        # complete body
        if not is_new_tx:
            body['error'] = {
                'message': self.ERROR_DEPOSIT_NOT_FOUND
            }
        else:
            body['error'] = {
                'message': self.ERROR_DEPOSIT_NOT_FOUND
            }
        return body