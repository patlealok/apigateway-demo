import json
import boto3

URL = "https://nnyp8jyyp7.execute-api.us-east-1.amazonaws.com/production"
gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url= URL)

def lambda_handler(event, context):
    # TODO implement
    connectionId= event["requestContext"].get("connectionId")
    msg = json.loads(event["body"])
    
    if 'message' in msg:
        msg= msg["message"]
        
        if msg.lower() == "car":
            r_msg = "car"
            post_message(connectionId, r_msg)
            return {'statusCode': 200}
        elif msg.lower()== "truck":
            r_msg = "truck"
            post_message(connectionId, r_msg)
            return {'statusCode': 200}
        elif msg.lower()== "banana":
            r_msg = "banana"
            post_message(connectionId, r_msg)
            return {'statusCode': 200}
            # TODO: write code...
        else:
            r_msg = "Incorrect message"
            post_message(connectionId, r_msg)
            return {'statusCode': 200}
            
    else:
        return {
        'statusCode': 200,
        'body': json.dumps("No message")
        #'body': json.dumps(event["requestContext"].get("connectionId"))
        }

def post_message(connectionId, msg):
    gateway_resp = gatewayapi.post_to_connection(ConnectionId=connectionId, Data=json.dumps({"message" : msg }))
'''
def lambda_handler(event, context):
    # TODO implement
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Message route invoked')
        #'body': json.dumps(event["requestContext"].get("connectionId"))
    }
'''