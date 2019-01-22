from http import HTTPStatus

from tornado import web


class BaseHandler(web.RequestHandler):
    def options(self, **kwargs):
        self.add_header("Access-Control-Allow-Methods", "PATCH, GET")
        self.add_header("Access-Control-Allow-Headers", "Authentication")
        self.writeResponse()

    def set_default_headers(self):
        self.add_header("Access-Control-Allow-Origin", "*")
        self.add_header("Content-Type", "application/json")

    def writeResponse(self, pCodigo=HTTPStatus.OK, pMensagem="Operação executada com sucesso!"):
        self.set_status(pCodigo)
        self.write({"status": pCodigo, "mensagem": pMensagem})
