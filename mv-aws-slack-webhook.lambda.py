#
#
#

import logging
import json
import os

from urllib.request import Request, urlopen
from urllib.error   import URLError, HTTPError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SLACK_URL     = os.environ['SLACK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL']

def lambda_handler(event, context):

    msg = {
        "text": "`" + str(event) + "`",
        "username": "AWS-Alerts: JSON",
        "mrkdwn": 'true'
    }

    send_to_slack(msg)


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



# main
lambda_handler( { 'Event': 'test' }, { 'Context': 'test' })

