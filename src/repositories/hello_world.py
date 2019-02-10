import json

from bson.json_util import dumps

from repositories import conexaomongo


class HelloWorldRepository():
    def __init__(self):
        self.conexao = conexaomongo

    async def salvar(self, msg):
        dado = dict()
        dado['msg'] = msg
        self.conexao.db.hello_world.insert_one(dado)

    async def consultar(self, filtro={}):
        resultado = self.conexao.db.hello_world.find(filtro)
        if resultado.count() == 0:
            return json.dumps({"msg": "Nada ainda, você precisa inserir algo!"})
        else:
            return dumps(resultado)
