## AWS Serverless Application Model Project

Creates an AWS SNS Topic, AWS SQS Queue, AWS IoT Rule and an AWS Lambda Function.
When a message is received from specified AWS IoT Core topics, it is forwarded to the SQS Queue. It is then transferred to the Lambda function with a delay. When the message is received, the function is triggered and sends and e-mail containing the message mody, send time (time the message was sent via MQTT) and the current time.
