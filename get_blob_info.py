from google.cloud import storage

def get_blob_info():
    client = storage.Client()
    mybucket = client.get_bucket(input("Enter bucket name >> "))
    myblob = mybucket.get_blob(input("Enter Blob Name >> "))
    print(myblob)

get_blob_info()




'''
This code lists a bucket's contents:

def get_bucket_objects():
    client = storage.Client()
    mybucket=client.get_bucket(input("Enter Bucket Name >> "))
    blobs = mybucket.list_blobs()
    print(list(blobs))

get_bucket_objects()

'''
