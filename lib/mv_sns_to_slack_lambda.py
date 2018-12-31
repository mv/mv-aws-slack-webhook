#
# Ref:
#   https://serverless.com/blog/serverless-cloudtrail-cloudwatch-events/
#   https://www.gorillastack.com/aws-cloudtrail-slack-integration/
#   https://api.slack.com/incoming-webhooks
#   https://api.slack.com/docs/message-attachments
#   https://api.slack.com/docs/message-buttons
#   https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html
#   https://docs.aws.amazon.com/sns/latest/dg/sns-message-and-json-formats.html#http-notification-json
#

import logging
import json
import os

from urllib.request import Request, urlopen
from urllib.error   import URLError, HTTPError

SLACK_URL     = os.environ['SLACK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):


    # check keys
    if 'eventName'         in event['Records'][0]:
        logger.info("Event: CloudTrail")
        msg = msg_cloudtrail(event)

    elif 'Sns'             in event['Records'][0]:
        logger.info("Event: SNS")
        msg = msg_sns(event)

    elif 'configRuleName'  in event:
        logger.info("Event: AWS Config")
        msg = event

    # check value
    elif 'Scheduled Event' == event.get('detail-type'):
        logger.info("Event: Scheduled Event")
        msg = event

    else:
        logger.info("Event: Others")
        msg = event

    send_to_slack( msg )
    send_to_slack(
    {
    "text": "`" + str(event) + "`",
    "username": "AWS-Alerts: JSON",
    "mrkdwn": 'true'
    })



def send_to_slack(msg, url=SLACK_URL):

    try:
        req = Request(SLACK_URL, json.dumps(msg).encode('utf-8'))
        response = urlopen(req)
        response.read()
        logger.info("Slack: [%s]", msg)

    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)

    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)



def msg_cloudtrail(ev):

    try:
        msg = ev['Records'][0]
        fields=[
            { 'title':'Account' , 'value': msg['userIdentity']['accountId'] , 'short': 'false' } ,
            { 'title':'Username', 'value': msg['userIdentity']['userName']  , 'short': 'false' } ,
            { 'title':'Service' , 'value': msg['eventSource']               , 'short': 'false' } ,
            { 'title':'Event'   , 'value': msg['eventName']                 , 'short': 'false' } ,
            { 'title':'Time'    , 'value': msg['eventTime']                 , 'short': 'false' } ,
            { 'title':'SourceIP', 'value': msg['sourceIPAddress']           , 'short': 'false' }
        ]

        text = "CloudTrail Event: {}".format( msg['eventName'] )
        attachments = [ {
            "fallback": text,
            "fields": fields,
            "color": "#2eb886",
            "footer": "Cloudtrail",
            "actions": [
                {
                    "type": "button",
                    "name": "Details",
                    "text": "JSON",
                    "value": 'eveveveve  veveve   eveve',
                    "confirm": {
                        "title": "JSON Event",
                        "text": str(ev)[0:40],
                        "ok_text": "Ok"
                    }
                }
            ]
        } ]

        return {
            "text": text,
            "attachments": attachments
        }


    except:
        return {
            "text": ev
        }


def msg_sns(ev):

    try:
        msg = ev['Records'][0]['Sns']['Message']
        text = "SNS Event: {}".format( msg['AlarmName'] )
        attachments = [ {
            "fallback": text,
            "fields": [
                { 'title':'Message' , 'value': msg['NewStateReason'] },
                { 'title':'Type'    , 'value': msg['NewStateValue']   , 'short': 'false' }
            ],
            "color": "#2eb886",
            "footer": "SNS",
            "actions": [
                {
                    "type": "button",
                    "name": "Details",
                    "text": "JSON",
                    "value": 'eveveveve  veveve   eveve',
                    "confirm": {
                        "title": "Are you sure?",
                        "text": "Wouldn't you prefer a good game of chess?",
                        "ok_text": "Yes",
                        "dismiss_text": "No"
                    }
                }
            ]
        } ]


        return {
            "text": text,
            "attachments": attachments
        }

    except:
        return ev


