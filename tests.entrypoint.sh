#!/bin/sh

pip3 install -r tests/functional/requirements.txt
pytest -p no:warnings --cov-report term-missing --cov=/code/app /code/tests
