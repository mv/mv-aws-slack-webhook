
import pytest
import os

from lib.mv_aws_slack_webhook_lambda import *


def test_lambda_handler():
    res = lambda_handler( {}, {})
    assert res['code'] == 200

def test_send_to_slack():
    SLACK_URL = os.environ['SLACK_URL']
#   res = send_to_slack( { 'message': 'this is a test' } )
#   assert res['code'] == 200
#   print(res)


