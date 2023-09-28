#!/bin/bash
# Makes a request to get a response from a certain URL
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
