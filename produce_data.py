import os, uuid
from minio import Minio

s3_endpoint = os.environ.get("S3_ENDPOINT")
s3_access_key= os.environ.get("S3_ACCESS_KEY")
s3_secret_key= os.environ.get("S3_SECRET_KEY")
object_key = os.environ.get("S3_OBJECT")

client = Minio(
    s3_endpoint,
    access_key=s3_access_key,
    secret_key=s3_secret_key,
)

print("object: ", object_key)

os.makedirs("data", exist_ok=True)

client.fget_object("amedemo", "mixed_0101_gradual.csv", "data/mixed_0101_gradual.csv")

