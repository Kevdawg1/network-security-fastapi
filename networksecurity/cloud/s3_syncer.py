"""
Requirements: 
1. `pip install awscli`
2. create IAM user, if does not exist
3. create access key
4. `aws configure`
5. copy and paste the access key and secret key
"""

import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        os.system(command)
        
    def sync_file_from_s3(self, file, aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {file}"
        os.system(command)