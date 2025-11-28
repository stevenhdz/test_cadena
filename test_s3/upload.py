import boto3

s3 = boto3.client("s3")

bucket_name = "mi-bucket-ejemplo"
file_path = "local/ruta/archivo.txt"
object_key = "uploads/archivo.txt"  # nombre dentro de S3

def subir_archivo():
    s3.upload_file(file_path, bucket_name, object_key)
    print(f"Subido a s3://{bucket_name}/{object_key}")

if __name__ == "__main__":
    subir_archivo()
