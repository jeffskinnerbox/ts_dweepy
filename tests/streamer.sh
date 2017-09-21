#!/bin/bash
set -e

# Used when testing ts_dweepy's streaming functionality to provide a simple
# background process that just sends dweets over and over again until told to
# stop.

BASE_URL="https://thingspace.io/dweet/for/"

# pass key in the url if 2nd cli arg is passed to script
if [ -z "$2" ]
    then
        key=""
    else
        key="?key=$2"
fi

for i in {1..10}; do
    curl -s -o output.txt -H "Content-Type: application/json" -d '{"hello":"world","somenum":6816513845}' $BASE_URL$1$key
    rm output.txt
    sleep 1
done
