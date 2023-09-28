#!/bin/bash
# Send a GET request to a given URL with an extra header field
curl -sL -H "X-School-User-Id: 98" "$1"
