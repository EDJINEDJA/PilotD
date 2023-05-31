#!bin/bash

echo "update the terminal"
sudo apt-get update

echo "upgrade the terminal"
sudo apt-get upgrade

echo "instaling dependancies"
pip install -r requirements.txt