# apigateway-demo
AWS apigateway demo project

How to use:

You need to connect with websocket URL using wscat.

If you want to trigger specific lambda fuction, you need to pass the parameter in json formate.

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
