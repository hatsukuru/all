# -*- coding:utf-8 -*-
'''
@File    : minio.py
@Time    : 2022/10/31 9:15
@Author  : hatsune
@Email   : l2011617078@163.com
@Software: PyCharm
'''
import minio

from minio import Minio
from minio.error import InvalidResponseError
from minio.error import S3Error
from all.settings import MINIO_CONF
try:
    client = Minio('140.24.1.107:29001',access_key='minioadmin',secret_key='minioadmin',secure=False)
    found = client.bucket_exists("pcdd")
except S3Error as e:
    print("error:", e)
print(found)# 返

import minio

minio_conf = {
    'endpoint': '140.24.1.107:29001',
    'access_key': 'minioadmin',
    'secret_key': 'minioadmin',
    'secure': False
}

def up_data_minio(bucket: str):
    client = minio.Minio(**minio_conf)
    client.fput_object(bucket_name=bucket, object_name='test2',
                       file_path='test.zip',
                       content_type='application/zip'
                       )

up_data_minio('pcdd')

'''
from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
    client.fput_object(
        "asiatrip", "asiaphotos-2015.zip", "/home/user/Photos/asiaphotos.zip",
    )
    print(
        "'/home/user/Photos/asiaphotos.zip' is successfully uploaded as "
        "object 'asiaphotos-2015.zip' to bucket 'asiatrip'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)'''
'''
def save_file(bucket, file_name, file_local_path):
    minio_client = Minio(
        "{0}:{1}".format("140.24.1.107", "29001"),
        secure=False,  # 默认True[https]
        access_key="minioadmin",
        secret_key="minioadmin",
    )
    minio_client.fput_object(bucket, file_name, file_local_path)



MINIO_CONF = {
    'endpoint': '140.24.1.107:29001',
    'access_key': 'minioadmin',
    'secret_key': 'minioadmin',
    'secure': False
}


def upload_minio(bucket:str,file_name:str,file_path):
    client = minio.Minio(**MINIO_CONF)
    client.fput_object(bucket_name=bucket, object_name=file_name,
                       file_path=file_path,
                       # content_type='application/zip'
                       content_type='application/text'
                       )

upload_minio(bucket="pcdd", file_name="aaaaaa.pdf", file_path=r"E:\aaaa\aaaaaa.pdf")'''