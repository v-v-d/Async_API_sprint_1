#!/bin/sh

pip3 install -r tests/functional/requirements.txt
pytest -p no:warnings
