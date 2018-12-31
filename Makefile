# vim:ft=make:ts=8:sts=8:sw=8:noet:tw=80:nowrap:list

# My vars
LAMBDA=mv-slack-webhook
VIRTUALENV=venv



###
### tasks
###
.PHONY: help vars

all: help

help:
	@echo
	@echo "Lambda: [${LAMBDA}]"
	@echo
	@echo "    make vars   - Defined vars for [${LAMBDA}]"
	@echo
	@echo "    make venv   - Create virtualenv: [${VIRTUALENV}]"
	@echo "    make req    - Install from 'requirements.txt'"
	@echo
	@echo "    make deploy - TODO: Lambda deploy: [${LAMBDA}]"
	@echo "    make test   - TODO: Run '...'"
	@echo


vars:
	@echo "Lambda:  [${LAMBDA}]"

venv:
	virtualenv ${VIRTUALENV}

venv_help:
	@echo
	@echo "source ${VIRTUALENV}/bin/activate"
	@echo

req:
	pip install -r requirements.txt

