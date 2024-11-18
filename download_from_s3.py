from tempfile import NamedTemporaryFile
import boto3


def download_s3_file(s3, bucket, s3_file_path, local_file_path=None):
    print(s3_file_path)
    if not local_file_path:
        local_file_path = NamedTemporaryFile(delete=False, mode='w').name
    s3.meta.client.download_file(bucket, s3_file_path, local_file_path)
    return local_file_path

def main():
    s3 = boto3.resource(
        's3',
        aws_access_key_id='',
        aws_secret_access_key=,
        region_name=
    )
    cloud_path = ''
    local_path = ''
    bucket = ''
    path = download_s3_file(s3 ,bucket ,cloud_path, local_path)
    print(path)

if __name__ == "__main__":
    main()
