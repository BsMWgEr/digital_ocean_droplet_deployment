import os

DJANGO_STORAGE_SERVICE = os.environ.get("DJANGO_STORAGE_SERVICE")
DJANGO_ROOT_NAME = os.environ.get("DJANGO_ROOT_NAME")
OBJECT_STORAGE_BUCKET = os.environ.get("OBJECT_STORAGE_BUCKET")
OBJECT_STORAGE_REGION = os.environ.get("OBJECT_STORAGE_REGION")
OBJECT_STORAGE_ACCESS_KEY = os.environ.get("OBJECT_STORAGE_ACCESS_KEY")
OBJECT_STORAGE_SECRET_KEY = os.environ.get("OBJECT_STORAGE_SECRET_KEY")
OBJECT_STORAGE_READY = all(
    [OBJECT_STORAGE_BUCKET, OBJECT_STORAGE_REGION, OBJECT_STORAGE_ACCESS_KEY, OBJECT_STORAGE_SECRET_KEY])

if OBJECT_STORAGE_READY:
    if DJANGO_STORAGE_SERVICE == "digitalocean":
        AWS_S3_ENDPOINT_URL = f"https://{OBJECT_STORAGE_REGION}.digitaloceanspaces.com"
    elif DJANGO_STORAGE_SERVICE == "linode":
        AWS_S3_ENDPOINT_URL = f"https://{OBJECT_STORAGE_REGION}.linodeobjects.com"
    else:
        AWS_S3_ENDPOINT_URL = f"https://{OBJECT_STORAGE_REGION}.amazonaws.com"
    AWS_ACCESS_KEY_ID = OBJECT_STORAGE_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = OBJECT_STORAGE_SECRET_KEY
    AWS_S3_REGION_NAME = OBJECT_STORAGE_REGION
    AWS_S3_USE_SSL = True
    AWS_STORAGE_BUCKET_NAME = OBJECT_STORAGE_BUCKET
    AWS_DEFAULT_ACL = "public-read"

    DEFAULT_FILE_STORAGE = f"{DJANGO_ROOT_NAME}.storages.backends.MediaS3BotoStorage"
    STATICFILES_STORAGE = f"{DJANGO_ROOT_NAME}.storages.backends.PublicS3Boto3Storage"
