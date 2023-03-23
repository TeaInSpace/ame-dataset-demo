import os, uuid


os.makedirs("data", exist_ok=True)

with open(file="data/output.txt", mode="w") as download_file:
 download_file.write("this is some data")
