import boto3

s3 = boto3.client("s3")

bucket_name = "mi-bucket-ejemplo"
object_key = "uploads/archivo.txt"
download_path = "descargas/archivo.txt"

def descargar_archivo():
    s3.download_file(bucket_name, object_key, download_path)
    print(f"Descargado en {download_path}")

if __name__ == "__main__":
    descargar_archivo()
