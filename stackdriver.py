#! python3

import os

import google.cloud.storage
from google.cloud import storage

storage_client = storage.Client.from_service_account_json(
            r'R:\OneDrive\Documents\es-test-204011-1ce7fb85b297.json')

bucket_name = 'es-test'
bucket      = storage_client.get_bucket(bucket_name)

source_file_name = r'R:\OneDrive - Individual Contract\Images\カメラ ロール\DSC_1121.JPG'
blob             = bucket.blob(os.path.basename(source_file_name))

blob.upload_from_filename(source_file_name)

print('File {} uploaded to {}.'.format(
    source_file_name,
    bucket
))


