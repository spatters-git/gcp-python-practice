# from https://cloud.google.com/storage/docs/creating-buckets#storage-create-bucket-python

from google.cloud import storage
def create_bucket(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)
    print('Bucket {} created'.format(bucket.name))

create_bucket('seanp-test-bucket')
