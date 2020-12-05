#!/bin/sh

sudo apt-get update &&\
sudo apt-get install python3 &&\
sudo apt-get install python3-pip &&\
sudo python3 -m pip install -r requirements.txt
