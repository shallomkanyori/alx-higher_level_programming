#!/bin/bash
# Displays the response body of a POST request to the given URL
curl -sL -X POST --data-urlencode "test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
