'''
Takes the filename to download as a command line argument
'''
from google.cloud import storage
from sys import argv

def download_from_bucket():
    script,filename = argv
    client = storage.Client()
    bucket = client.get_bucket(input("Enter Bucket Name >> "))
    blob = bucket.get_blob(filename)
    print(f"Downloading {filename}")
    blob.download_to_file(open(filename,"wb"))


download_from_bucket()
