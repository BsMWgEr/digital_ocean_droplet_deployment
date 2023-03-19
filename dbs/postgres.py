import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

POSTGRES_DB_IS_AVAIL = all([
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PORT
])

POSTGRES_DB_REQUIRE_SSL = os.environ.get("POSTGRES_DB_REQUIRE_SSL")
POSTGRES_DB_CERT_PATH = BASE_DIR / "certs" / "db.crt"

if POSTGRES_DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
        }
    }
    if POSTGRES_DB_REQUIRE_SSL:
        DATABASES["default"]["OPTIONS"] = {
            "sslmode": "require",
        }
