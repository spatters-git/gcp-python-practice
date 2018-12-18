'''
See Create Bucket code for reference:
from google.cloud import storage
def create_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print('Bucket {} created'.format(bucket.name))

create_bucket('seanp-test-bucket')
'''

from google.cloud import storage

def list_buckets():
    storage_client = storage.Client()
    buckets = []
    for bucket in storage_client.list_buckets():
        buckets.append(bucket.name)
    print(buckets)


list_buckets()
