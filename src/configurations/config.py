from decouple import config

SERVER_PORTA_EXECUCAO = config("APP_PORT", default=5001, cast=int)
HOST = config("HOST", default="127.0.0.1", cast=str)

CONF_DB = config("CONF_DB", default="TestDocker", cast=str)

CONF_DEBUG = config("CONF_DEBUG", default=True, cast=bool)
CONF_FULL_URL = config("CONF_FULL_URL", default=True, cast=bool)
CONF_COMPRESS_RESPONSE = config("CONF_COMPRESS_RESPONSE", default=True, cast=bool)

