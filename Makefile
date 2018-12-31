# vim:ft=make:ts=8:sts=8:sw=8:noet:tw=80:nowrap:list

# My vars
_lambda=mv-slack-webhook
_virtualenv=venv

SLACK_URL:=$(shell echo ${SLACK_URL} )
SLACK_CHANNEL:=$(shell echo ${SLACK_CHANNEL} )


###
### tasks
###
.PHONY: help show

all: help

help:
	@echo
	@echo "Lambda: [${_lambda}]"
	@echo
	@echo "  make show   - Show env vars for [${_lambda}]"
	@echo
	@echo "  make venv   - Create virtualenv: [${_virtualenv}]"
	@echo "  make req    - Install from 'requirements.txt'"
	@echo
	@echo "  make deploy - TODO: Lambda deploy: [${_lambda}]"
	@echo "  make test   - TODO: Run '...'"
	@echo "  make tst    - run via command-line"
	@echo


show:
	@echo
	@echo "  SLACK_URL:     [${SLACK_URL}]"
	@echo "  SLACK_CHANNEL: [${SLACK_CHANNEL}]"
	@echo

venv:
	virtualenv ${_virtualenv}

venv_clear:
	@echo "Reinstalling..."
	virtualenv ${_virtualenv} --clear

venv_help:
	@echo
	@echo "source ${_virtualenv}/bin/activate"
	@echo

req:
	pip install -r requirements.txt


tst:
	python ./mv-aws-slack-webhook.lambda.py

