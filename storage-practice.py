from google.cloud import storage
client = storage.Client()
#https://console.cloud.google.com/storage/browser/sean-cloud-storage-test-bucket/
bucket = client.get_bucket('sean-cloud-storage-test-bucket')
# Then do other things...
blob = bucket.get_blob('ITTD certificate.pdf')
print(dir(blob))
print(len(blob.download_as_string()))
blob.download_to_file(open("blob.dat","wb"))
#blob.upload_from_string('New contents!')
'''
blob2 = bucket.blob('cal')
blob2.upload_from_filename(filename='x')
'''
c2=storage.Client(project='xvaliant-student-208012')
print(dir(c2))
