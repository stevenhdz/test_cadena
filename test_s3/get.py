import boto3

s3 = boto3.client("s3")

def obtener_contenido(bucket: str, key: str) -> bytes:
    response = s3.get_object(Bucket=bucket, Key=key)
    return response["Body"].read()

contenido = obtener_contenido("mi-bucket-ejemplo", "uploads/archivo.txt")
print(contenido.decode("utf-8"))
