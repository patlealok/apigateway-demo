import json
import boto3

URL = "https://nnyp8jyyp7.execute-api.us-east-1.amazonaws.com/production"
gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url= URL)

def lambda_handler(event, context):
    # TODO implement
    connectionId= event["requestContext"].get("connectionId")
    msg = json.loads(event["body"])
    client1 = boto3.client("dynamodb")
    #client1.put_item(TableName="query_string", Item={"word": { "S" : msg })
    response = client1.scan(TableName="query_string")
    #connection = response["Items"]

    for connection in response["Items"]:
        msg1= msg["message"]
        if msg1.lower() == connection["word"]["S"]:
            response = gatewayapi.post_to_connection(ConnectionId=connectionId, Data=json.dumps({"message" : msg1 }))
            
    return {
        'statusCode': 200,
        'body': json.dumps('Request completed ! Thanks')
        }

