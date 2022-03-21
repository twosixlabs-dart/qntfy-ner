#!/usr/bin/env sh

set -e

# Download and install project dependencies
# Assumes pip present and access to gitlab.qntfy.com
python -m pip install --upgrade pip pytest
python setup.py install
# due to some annoyances with private repos, need this
python -m spacy download en_core_web_lg
