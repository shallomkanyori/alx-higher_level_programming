#!/bin/bash
# Displays all HTTP methods a server will accept given a URL
curl -sI -X OPTIONS "$1" | grep 'Allow:' | sed 's/\r//g' | cut -d " " -f 2-
