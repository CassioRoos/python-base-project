from decouple import config

SERVER_PORTA_EXECUCAO = config("APP_PORT", default=5001, cast=int)

CONS_SECRET = "?????"
HOST = config("HOST", default="LOCALHOST", cast=str)
CONF_DB = config("CONF_DB", default="TestDocker", cast=str)

CONF_DEBUG = config("CONF_DEBUG", default=True, cast=bool)
CONF_FULL_URL = config("CONF_FULL_URL", default=True, cast=bool)
CONF_COMPRESS_RESPONSE = config("CONF_COMPRESS_RESPONSE", default=True, cast=bool)

JWT_AUTENTICACAO_ATIVA = config("JWT_AUTENTICACAO_ATIVA", default=True, cast=bool)
JWT_MOCK_TOKEN_RAW = config("JWT_MOCK_TOKEN_RAW", default="", cast=str)
