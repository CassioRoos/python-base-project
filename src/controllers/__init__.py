from tornado import web

from src.configurations import config, uris
from src.controllers.hello_world import HelloWorld


class PainelTarefasApplication(web.Application):
    def __init__(self, classes):
        url_handlers = [(uris.URI_CONTEXTO_HELLO_WORLD, HelloWorld)]
        settings = {
            "debug": config.CONF_DEBUG,
            "use_full_url": config.CONF_FULL_URL,
            **classes,
            "compress_response": config.CONF_COMPRESS_RESPONSE
        }
        super().__init__(url_handlers, **settings)
