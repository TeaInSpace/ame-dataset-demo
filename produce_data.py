import os, uuid
from minio import Minio

s3_endpoint = os.environ.get("S3_ENDPOINT")
s3_access_key= os.environ.get("S3_ACCESS_KEY")
s3_secret_key= os.environ.get("S3_SECRET_KEY")

client = Minio(
    s3_endpoint,
    access_key=s3_access_key,
    secret_key=s3_secret_key,
)

os.makedirs("data", exist_ok=True)

client.fget_object("amedemo", "mixed_0101_gradual.csv", "mixed_0101_gradual.csv")

with open(file="data/output.txt", mode="w") as download_file:
 download_file.write("this is some data")
