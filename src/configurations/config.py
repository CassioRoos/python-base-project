from decouple import config

APP_PORT = config("APP_PORT", cast=int)
HOST = config("HOST", default="127.0.0.1", cast=str)

DB_URL = config("DB_URL", cast=str)
DB_PORTA = config("DB_PORTA", cast=int)
DB_NOME = config("DB_NOME", cast=str)

CONF_DEBUG = config("CONF_DEBUG", default=True, cast=bool)
CONF_FULL_URL = config("CONF_FULL_URL", default=True, cast=bool)
CONF_COMPRESS_RESPONSE = config("CONF_COMPRESS_RESPONSE", default=True, cast=bool)

