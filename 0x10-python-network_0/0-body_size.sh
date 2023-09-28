#!/usr/bin/bash
# Displays the body size of the response from a request to a given URL
if [ $# -ne 0 ]; then
	curl -sI "$1" | grep 'Content-Length:' | sed 's/\r//g' | cut -d " " -f 2
fi
