#!/bin/bash
# get respose body
curl -s -w "%{http_code}" "$url" | awk 'END { if ($0 == 200) print $0 }'
