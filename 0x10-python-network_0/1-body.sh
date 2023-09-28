#!/bin/bash
# Displays the response body of a GET request to a given URL
out=$(curl -sL -w "%{http_code}" "$1"); [ "${out: -3}" -eq 200 ] && printf %s "$out" | sed -E '$ s/.{3}$//'
