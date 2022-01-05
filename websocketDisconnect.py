import json
import boto3

def lambda_handler(event, context):
    client1 = boto3.client("dynamodb")
    client1.delete_item(TableName="websocket", Key={"websocket_connectionid":{"S": event["requestContext"].get("connectionId")}})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
