# apigateway-demo
AWS apigateway demo project

apigateway routes -

Route - lambda function
---------------------------
$connect - websocketConnect
$disconnect - websocketDisconnect
websocket-dynamo - websocketdefault
websocket-message - websocket-message
$default - websocketdefault

How to use:

You need to connect with websocket URL using wscat.

If you want to trigger specific lambda fuction (websocket-dynamo), you need to pass the parameter in json formate.

{ "action" : "websocket-dynamo" , "message" : "car" }

As per requirement, using websocket URL, trigger the lambda fuction which will check if random word is matched with dynamo DB record (car, truck and banana) then same word will return otherwise it will return blank.

Please find the evidence.

with matched record -

> { "action" : "websocket-dynamo" , "message" : "car" }
< {"message": "car"}

No match -

> { "action" : "websocket-dynamo" , "message" : "tea" }
< "Request completed ! Thanks"


[cloudshell-user@ip-10-0-101-67 ~]$ wscat -c wss://nnyp8jyyp7.execute-api.us-east-1.amazonaws.com/production
Connected (press CTRL+C to quit)
> { "action" : "websocket-dynamo" , "message" : "car" }
< {"message": "car"}
< "Request completed ! Thanks"
> { "action" : "websocket-dynamo" , "message" : "tea" }
< "Request completed ! Thanks"



Few extra exercise:

When you connect with websocket URL, websocketConnect lamda function will trigger to insert the connection id.

[cloudshell-user@ip-10-0-45-254 ~]$ wscat -c wss://nnyp8jyyp7.execute-api.us-east-1.amazonaws.com/production
Connected (press CTRL+C to quit)
[cloudshell-user@ip-10-0-45-254 ~]$ 

when you disconnect the session, websocketDisconnect lamda function will trigger to remove the same connection id.

