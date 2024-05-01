#!/bin/bash
# A script that sends a POST request displaying the response
curl -sX POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
