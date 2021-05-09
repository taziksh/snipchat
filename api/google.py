from google.cloud import storage

import os

class Cloud:
  def __init__(self, SERVICE_ACCOUNT_PATH='./snipchat.json'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACCOUNT_PATH 

  #TODO: modified official docs. make a PR
  def create_bucket_class_location(self, bucket):
      """Create a new bucket in specific location with storage class"""
      # bucket = "your-new-bucket-name"

      storage_client = storage.Client()

      new_bucket = storage_client.create_bucket(bucket)

      print(
          "Created bucket {} in {} with storage class {}".format(
              new_bucket.name, new_bucket.location, new_bucket.storage_class
          )
      )
      return new_bucket


  def upload_blob(self, bucket, source_file, destination_blob):
      """Uploads a file to the bucket."""
      # The ID of your GCS bucket
      # bucket = "your-bucket-name"
      # The path to your file to upload
      # source_file = "local/path/to/file"
      # The ID of your GCS object
      # destination_blob = "storage-object-name"

      storage_client = storage.Client()
      bucket = storage_client.bucket(bucket)
      blob = bucket.blob(destination_blob)

      blob.upload_from_filename(source_file)

      print(
          "File {} uploaded to {}.".format(
              source_file, destination_blob
          )
      )

  def make_blob_public(self, bucket, blob):
      """Makes a blob publicly accessible."""
      # bucket = "your-bucket-name"
      # blob = "your-object-name"

      storage_client = storage.Client()
      bucket = storage_client.bucket(bucket)
      blob = bucket.blob(blob)

      blob.make_public()

      print(
          "Blob {} is publicly accessible at {}".format(
              blob.name, blob.public_url
          )
      )
      return blob.public_url
