from pydoc_data.topics import topics
import boto3
from datetime import datetime
import json

def lambda_handler(event, context):

    print("Function triggered.")

    snsClient = boto3.client("sns")

    print(event)

    body = json.loads(event["Records"][0]["body"])["message"]
    send_time = datetime.fromtimestamp(int(event["Records"][0]["attributes"]["SentTimestamp"])/1000)
    sender = event["Records"][0]["attributes"]["SenderId"]

    message = f"{body}\n   Send Time: {send_time}\n   Redirect Time: {datetime.now()}\n   Sender ID: {sender}"

    tpcs = snsClient.list_topics()
    topicArn = tpcs["Topics"][0]["TopicArn"]
    for t in tpcs["Topics"]:
        if snsClient.get_topic_attributes(TopicArn=t["TopicArn"])["Attributes"]["DisplayName"] == "send_mail":
            topicArn = t["TopicArn"]

    response = snsClient.publish(
        # TargetArn=    ???
        TopicArn=topicArn,
        Message=message,
        Subject="New MQTT Message"
    )

    return {
        "statusCode": 200,
        "response": response
    }