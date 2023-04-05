#!/bin/bash

echo "setup venomizer"
sudo apt update
sudo apt install git
sudo apt install python3
sudo apt install pip
sudo pip3 install -r requirements.txt
sudo python3 setup.py
