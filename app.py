import asyncio
import logging.config
import socket

import tornado
import yaml

from src.configurations import config
from src.controllers import PainelTarefasApplication

hostname = socket.gethostname()
IP = config.HOST

with open('logging.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())
    logging.config.dictConfig(log_cfg)


def log_request(handler):
    if handler.get_status() < 400:
        log_method = logging.info
    elif handler.get_status() < 500:
        log_method = logging.warning
    else:
        log_method = logging.error

    request_time = 1000.0 * handler.request.request_time()
    usuario = ''
    if hasattr(handler, 'usuario'):
        usuario = handler.usuario
    extradict = {
        "usuario": usuario,
        "metodo": handler.request.method,
        "caminho": handler.request.path,
        "status": handler.get_status(),
        "ip_remoto": handler.request.remote_ip,
        "uri": handler.request.uri,
        "tempo_request": request_time}

    camposlog = "{usuario:<10} {metodo:<8} {caminho:<20} {status:<4} {ip_remoto:<17}" \
                " {uri} {tempo_request}"
    log_method(camposlog.format(**extradict), extra=extradict)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    """ Configurações passadas para a base do handler """
    classes = {}
    app = PainelTarefasApplication(classes)
    app.log_request = log_request
    porta = config.SERVER_PORTA_EXECUCAO
    app.listen(porta)
    print(f"Servidor rodando em http://{IP}:{porta}. Pressione Ctrl + C para parar.")
    tornado.ioloop.IOLoop.current().start()
