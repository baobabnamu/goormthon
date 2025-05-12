#!/bin/bash
echo "Running test script with argument: $1" > cmdTestResult.txt
nginx -g 'daemon off;'