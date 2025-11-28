import json
import uuid
from datetime import datetime

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Todos")  # nombre de la tabla


def lambda_handler(event, context):
    try:
        # Body viene como string desde API Gateway
        body = json.loads(event.get("body") or "{}")

        title = body.get("title")
        if not title:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "title is required"}),
            }

        todo_id = str(uuid.uuid4())

        item = {
            "id": todo_id,
            "title": title,
            "done": False,
            "createdAt": datetime.utcnow().isoformat() + "Z",
        }

        table.put_item(Item=item)

        return {
            "statusCode": 201,
            "body": json.dumps(item),
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal Server Error"}),
        }
