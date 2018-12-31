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

#   send_to_slack(msg)

    return {
        'code': 200
    }


def send_to_slack(msg, url=SLACK_URL):

    try:
        logger.info("Slack: [%s]", msg)
        print("Slack: [%s]", msg)
        print('Url: {}'.format(SLACK_URL))

        req = Request(SLACK_URL, json.dumps(msg).encode('utf-8'))
        res = urlopen(req)
        res.read()
#       res = { 'code': 200, 'message': 'x'}
        return {
            'code':    res.code,
            'message': res.msg
        }


    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)

    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)



# main

#if __name__ == "__main__":
#    lambda_handler( { 'Event': 'test' }, { 'Context': 'test' })

msg = { 'Event': 'test' }
send_to_slack( msg )


