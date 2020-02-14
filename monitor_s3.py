import boto3
import hashlib
import os


s3 = boto3.resource('s3')
storage = boto3.client('s3')
BUCKET_NAME = 'python-example-bucket1'

while True:
    bucket = s3.Bucket(BUCKET_NAME)
    for obj in bucket.objects.all():
        print(obj)
        if "#" in obj.key:
            print ("Downloading a file")
            storage.download_file (BUCKET_NAME, obj.key, "/tmp/index.html")
            hash_key = obj.key
            hash_key = hash_key [1 : : ]
            with open("/tmp/index.html","rb") as f:
                bytes = f.read() # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest();
                print(readable_hash)
                hash_key = hash_key + "/hash"
                print(hash_key)

            with open ("/tmp/hash", "w") as f:
                f.write(readable_hash)

            storage.upload_file ("/tmp/hash", BUCKET_NAME, hash_key)
            storage.delete_object (Bucket=BUCKET_NAME, Key = obj.key)
            os.remove ("/tmp/index.html")
            os.remove ("/tmp/hash")
        else:
            print ("Doing Nothing")


