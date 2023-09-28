#!/bin/bash
# Displays the response body of a POST request with JSON to the given URL
curl -sL -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
