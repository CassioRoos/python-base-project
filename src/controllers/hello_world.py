import time
from http import HTTPStatus
from random import randint

from services.hello_world import HelloWorld
from src.controllers.base import BaseHandler

helloworldservice = HelloWorld()


class HelloWorld(BaseHandler):
    async def get(self):
        time.sleep(randint(1, 3))
        dados = await helloworldservice.pegar_dados_salvos()
        return self.writeResponse(HTTPStatus.OK, dados)

    async def post(self):
        await helloworldservice.salvar_dados(self.request.body)
        return self.writeResponse(HTTPStatus.OK, "Um novo registro inserido no mongo")
