'''
See: https://googleapis.github.io/google-cloud-python/latest/storage/buckets.html

'''

from google.cloud import storage

def get_bucket_objects():
    client = storage.Client()
    mybucket=client.get_bucket(input("Enter Bucket Name >> "))
    blobs = mybucket.list_blobs()
    print(list(blobs))

get_bucket_objects() 




