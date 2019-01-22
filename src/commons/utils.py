import jwt

from src.configurations import config


def logar_metodo(pfunc):
    import logging
    import time

    logger = logging.getLogger(__name__)

    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcname = pfunc.__name__
        logger.debug(f"{funcname} chamada com esses *ards {args}  e esses **kwards{kwargs}")
        try:
            result = pfunc(*args, **kwargs)
        except Exception as error:
            logger(type(error))
            logger.debug(error)
            raise error
        logger.debug(f"{funcname} resultou: {result}")
        fim = time.time() - inicio
        logger.debug(f"{funcname} rodou em {fim}")
        return result

    return wrapper


def decodificar_token(token):
    return jwt.decode(token, config.CONS_SECRET, algorithms=["HS512"], verify=True)
