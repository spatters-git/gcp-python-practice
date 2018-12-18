'''
takes filename as command line argument
'''

from google.cloud import storage
from sys import argv

def upload_blob():
    client = storage.Client()
    script, blobname = argv
    bucket = client.get_bucket(input("Enter Bucket Name >> "))
    blob = bucket.get_blob(blobname)
    print(f"Uploading {blobname}")
    upblob = bucket.blob(blobname)
    upblob.upload_from_filename(filename=blobname)


upload_blob()



