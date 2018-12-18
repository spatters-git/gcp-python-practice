'''
Adapted from download_blob.py, attempts to get the filename to download via user input
Fails.  The blob variable is being set to None...why?
Errors:
(py3-6-lab) cloud-storage-practice $ python download_blob2.py 
Enter Bucket Name >> seanp-test-bucket
Which blob do you want to download?
[<Blob: seanp-test-bucket, Beneficiary Fidelity.pdf>, <Blob: seanp-test-bucket, ITTD certificate.pdf>, <Blob: seanp-test-bucket, Kelly EO License Application.pdf>, <Blob: seanp-test-bucket, blob.dat>, <Blob: seanp-test-bucket, blob.pdf>, <Blob: seanp-test-bucket, blobname>]
Enter Blob Name >> "blobname"
Downloading None
Traceback (most recent call last):
  File "download_blob2.py", line 20, in <module>
    download_from_bucket()
  File "download_blob2.py", line 17, in download_from_bucket
    blob.download_to_file(open(blob,"wb"))
AttributeError: 'NoneType' object has no attribute 'download_to_file'


'''
from google.cloud import storage
from sys import argv

def download_from_bucket():
#   script,filename = argv
    client = storage.Client()
    bucket = client.get_bucket(input("Enter Bucket Name >> "))
    blobs = bucket.list_blobs()
    print("Which blob do you want to download?")
    print(list(blobs))
    blob = bucket.get_blob(input("Enter Blob Name >> "))
    print(f"Downloading {blob}")
    blob.download_to_file(open(blob,"wb"))


download_from_bucket()
