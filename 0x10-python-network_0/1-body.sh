#!/bin/bash
# Displays the response body of a GET request to a given URL
out=$(curl -s -w "%{http_code}" "$1"); [ "${out: -3}" -eq 200 ] && echo "$out" | sed '$d'
