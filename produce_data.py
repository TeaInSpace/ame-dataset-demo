# import os, uuid
# from minio import Minio
import os, sys

# s3_endpoint = os.environ.get("S3_ENDPOINT")
# s3_access_key= os.environ.get("S3_ACCESS_KEY")
# s3_secret_key= os.environ.get("S3_SECRET_KEY")
# object_key = os.environ.get("S3_OBJECT")

# client = Minio(
#     s3_endpoint,
#     access_key=s3_access_key,
#     secret_key=s3_secret_key,
# )

# print("object: ", object_key)


# client.fget_object("amedemo", object_key, "data/mixed_0101_gradual.csv")


os.makedirs("data", exist_ok=True)

with open('./data/myartifact.txt', 'w', encoding='utf-8') as f:
    for a in sys.argv[1:]:
        f.write("mydata")



