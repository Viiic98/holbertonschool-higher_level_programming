#!/bin/bash
# Number of bytes of the content
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
