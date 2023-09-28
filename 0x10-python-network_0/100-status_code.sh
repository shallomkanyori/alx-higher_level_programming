#!/bin/bash
# Displays the status code of a request to a given URL
curl -sL -o /dev/null -w "%{http_code}" "$1"
