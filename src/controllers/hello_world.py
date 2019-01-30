import time
from http import HTTPStatus
from random import randint

from src.controllers.base import BaseHandler


class HelloWorld(BaseHandler):
    async def get(self):
        time.sleep(randint(1, 7))
        return self.writeResponse(HTTPStatus.OK, f"HELLO FROM DOCKER")
