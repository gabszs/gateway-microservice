# Documentation for `object_storage.py`

## Overview

This module provides an asynchronous interface for interacting with Amazon S3 object storage using the aiobotocore library. The primary class, `AsyncS3Manager`, facilitates operations such as checking bucket existence, uploading, downloading, deleting objects, and listing objects within a bucket.

## Class: `AsyncS3Manager`

This class is designed to manage interactions with an S3-compatible object storage using asynchronous operations. It leverages `aiobotocore`, an asynchronous wrapper for `boto3`, to perform non-blocking operations on S3.

### Initialization

```python
def __init__(
    self,
    s3_access_key_id: str = settings.s3_access_key,
    s3_secret_access_key: str = settings.s3_secret_key,
    region_name: str = "auto",
    endpoint_url: str = settings.s3_endpoint,
):
    ...
```

- **Parameters:**
  - `s3_access_key_id` (str): AWS access key ID used for authentication. Defaults to the value from `settings.s3_access_key`.
  - `s3_secret_access_key` (str): AWS secret access key used for authentication. Defaults to the value from `settings.s3_secret_key`.
  - `region_name` (str): AWS region where the S3 bucket is located. Defaults to `"auto"`, which uses aiobotocore's automatic region detection.
  - `endpoint_url` (str): URL of the S3 endpoint, useful for S3-compatible services. Defaults to the value from `settings.s3_endpoint`.

- **Attributes:**
  - `session`: An aiobotocore session used to create clients for S3 interactions.

### Private Method: `_create_client`

```python
async def _create_client(self):
    ...
```

- **Description:** 
  - Creates and returns an asynchronous S3 client using the provided credentials, region, and endpoint URL.
- **Returns:** 
  - An aiobotocore S3 client.

### Method: `bucket_exists`

```python
async def bucket_exists(self, bucket_name: str) -> bool:
    ...
```

- **Description:** 
  - Checks if a given bucket exists within the S3 service.
- **Parameters:**
  - `bucket_name` (str): The name of the bucket to check.
- **Returns:** 
  - `True` if the bucket exists, `False` otherwise.

### Method: `put_object`

```python
async def put_object(self, bucket_name: str, key: str, data: bytes) -> dict:
    ...
```

- **Description:** 
  - Uploads an object to a specified bucket with the provided key and data.
- **Parameters:**
  - `bucket_name` (str): The name of the bucket to upload the object to.
  - `key` (str): The key (or path) within the bucket for the object.
  - `data` (bytes): The binary data of the object to upload.
- **Returns:** 
  - A dictionary containing the response from the S3 service upon successful upload.

### Method: `get_object`

```python
async def get_object(self, bucket_name: str, key: str) -> dict:
    ...
```

- **Description:** 
  - Retrieves an object from a specified bucket using the provided key.
- **Parameters:**
  - `bucket_name` (str): The name of the bucket to fetch the object from.
  - `key` (str): The key (or path) within the bucket for the object.
- **Returns:** 
  - A dictionary containing the object's content and content type.

### Method: `delete_object`

```python
async def delete_object(self, bucket_name: str, key: str) -> dict:
    ...
```

- **Description:** 
  - Deletes an object from a specified bucket using the provided key.
- **Parameters:**
  - `bucket_name` (str): The name of the bucket from which the object will be deleted.
  - `key` (str): The key (or path) within the bucket for the object to delete.
- **Returns:** 
  - A dictionary containing the response from the S3 service upon successful deletion.

### Method: `list_objects`

```python
async def list_objects(self, bucket_name: str, prefix: str) -> list:
    ...
```

- **Description:** 
  - Lists objects in a specified bucket that match a given prefix.
- **Parameters:**
  - `bucket_name` (str): The name of the bucket to list objects from.
  - `prefix` (str): The prefix to filter the objects to list.
- **Returns:** 
  - A list of dictionaries, each representing an object that matches the given prefix.

## Key Concepts

- **Asynchronous Operations:** The class methods are asynchronous, allowing non-blocking operations when interacting with S3. This is crucial for high-performance applications that require efficient I/O operations.
- **S3 Compatibility:** The module is designed to work with any S3-compatible storage by allowing customizable endpoints and regions, making it versatile for cloud and on-premise storage solutions.

This file is a utility designed for seamless integration with S3 object storage, providing a straightforward API for common storage operations while ensuring asynchronous execution for performance optimization.