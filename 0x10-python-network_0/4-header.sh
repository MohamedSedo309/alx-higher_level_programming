#!/bin/bash
# Take in URL, add header variable, displays hello world
curl -s -H "X-School-User-Id":98 "$1"
