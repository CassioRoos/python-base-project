import json

from repositories.hello_world import HelloWorldRepository

helloworldrepository = HelloWorldRepository()


class HelloWorld():
    def __init__(self):
        self.banco = helloworldrepository

    async def _importthis(self):
        import contextlib, io
        zen = io.StringIO()
        with contextlib.redirect_stdout(zen):
            import this
        return zen.getvalue().split('.')

    async def salvar_dados(self, body):
        if not body:
            msg = await self._importthis()
        else:
            msg = json.loads(body)

        await self.banco.salvar(msg)

    async def pegar_dados_salvos(self):
        resultado = await self.banco.consultar()
        return json.loads(resultado)
