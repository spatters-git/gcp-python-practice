from google.cloud import storage
from sys import argv

def list_buckets():
    storage_client = storage.Client()
    buckets = []
    for bucket in storage_client.list_buckets():
        buckets.append(bucket.name)
    return(buckets)

def bucket_exists():
    storage_client = storage.Client()
    script, file = argv
    bucket = storage_client.get_bucket(input("Enter Bucket Name >> "))
    strbucket = str(bucket)
    bucketname = strbucket[9:-1]

    if bucketname in list_buckets():
        print(f"{bucketname} Exists!")
        blob = bucket.get_blob(file)
        print(f"Uploading {file}")
        upblob = bucket.blob(file)
        upblob.upload_from_filename(filename=file)

        manipulate_objects(bucketname)
  
    else:
        print("Bucket does not exist")

def manipulate_objects(bucket):
    client = storage.Client()
    mybucket = client.get_bucket(bucket)
    destbucket = client.get_bucket(input("Enter Destination Bucket Name >> "))
    blobs = mybucket.list_blobs()
    destblobs = destbucket.list_blobs()
    script,file = argv
    bloblist = list(blobs)
    destbloblist = list(destblobs)
    for blob in bloblist:
        if blob.name == file:
            print(f"File {file} found, copying")
            new_blob = mybucket.copy_blob(blob, destbucket, blob.name)
    print(f"Contents of {mybucket.name}: {bloblist}")
    print(f"Contents of {destbucket.name}: {destbloblist}")
    choice = input(f"Would you like to delete the file from {mybucket.name}? (Y or N) >>")
    if choice == "Y" or choice == "y" or choice == "yes":
        delblob = mybucket.blob(file)
        delblob.delete()
        print(f"{delblob.name} deleted from {mybucket.name}")
          

bucket_exists()
