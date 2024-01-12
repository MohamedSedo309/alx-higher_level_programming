#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Please provide a file name as an argument."
  exit 1
fi

filename=$1

# Create the file
touch "$filename"

# Set the permissions to u+x
chmod u+x "$filename"

echo "File '$filename' created with permissions u+x."

# Open the file using Emacs
emacs "$filename"
