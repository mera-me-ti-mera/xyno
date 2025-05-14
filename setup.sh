#!/bin/bash
set -eux -o pipefail

sudo apt-get update
sudo apt-get install -y tree python3-venv
python -m venv venv
./venv/bin/pip3 install scrapy
