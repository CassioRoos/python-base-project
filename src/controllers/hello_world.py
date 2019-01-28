import time
from http import HTTPStatus
from random import randint
from src.configurations import config

from src.controllers.base import BaseHandler


class HelloWorld(BaseHandler):
    async def get(self):
        time.sleep(randint(1, 7))
        return self.writeResponse(HTTPStatus.OK, f"HELLO WORLD! From APP {config.APP_ID}")
