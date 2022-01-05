import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client1 = boto3.client("dynamodb")
    client1.put_item(TableName="websocket", Item={"websocket_connectionid":{"S": event["requestContext"].get("connectionId")}})
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
