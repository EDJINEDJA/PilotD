#!bin/bash
set -o errexit
echo "update the terminal"
sudo apt-get update

echo "upgrade the terminal"
sudo apt-get upgrade

echo "apdate pip"
pip install --upgrade

echo "instaling dependancies"
pip install -r requirements.txt