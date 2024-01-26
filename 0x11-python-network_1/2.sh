#!/bin/bash

# Check if a file name is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a file name as an argument."
  exit 1
fi

# Extract the first character from the file name
first_char=$(echo "$1" | cut -c1)

# Perform Git operations
git add "$1"
git_status=$?
if [ $git_status -ne 0 ]; then
  echo "Git add failed with error code: $git_status"
  exit 1
fi

commit_message="task $first_char"
git commit -m "$commit_message"
git_status=$?
if [ $git_status -ne 0 ]; then
  echo "Git commit failed with error code: $git_status"
  exit 1
fi

git push
git_status=$?
if [ $git_status -ne 0 ]; then
  echo "Git push failed with error code: $git_status"
  exit 1
fi

echo "Git operations completed successfully."
