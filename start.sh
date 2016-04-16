#!/bin/bash
# Requires: chmod u+x start.sh

# sudo apt-get update
# sudo apt-get install -y nodejs npm
# sudo npm i -g forever
# forever start ~/start.sh

nohup python ~/Desktop/Ds18b20/read.py &

# Kill it:
# ps -ef |grep python
# kill xxx