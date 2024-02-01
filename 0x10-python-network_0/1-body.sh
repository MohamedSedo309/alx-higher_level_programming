#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Send a GET request to the URL and store the response in a variable
response=$(curl -s -w "%{http_code}" "$url")

# Extract the status code
status_code=$(echo "$response" | tail -n1)

# Check if the status code is 200
if [ "$status_code" -eq 200 ]; then
  # Extract and display the body of the response
  body=$(echo "$response" | sed '$d')
  echo "$body"
else
  echo "Request failed with status code: $status_code"
fi
