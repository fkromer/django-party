#!/bin/bash
rm -rf $PWD/venv
python3.12 -m venv venv
source "$PWD/../venv/bin/python"
pip install -r requirements.txt