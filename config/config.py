import secrets


class Config:
    DEBUG = True

    TEMPLATES_AUTO_RELOAD = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://studi_admin:Password!1234@postgresql-studi.alwaysdata.net/studi_mercadona_def'

    SECRET_KEY = secrets.token_hex(32)

