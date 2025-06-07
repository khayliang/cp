#!/bin/bash

# Check if filename is provided
if [ -z "$1" ]; then
  echo "Usage: $0 filepath"
  exit 1
fi

filepath="$1"

# Check if file exists
if [ ! -f "$filepath" ]; then
  echo "File '$filepath' not found!"
  exit 1
fi

mkdir -p ./build

res=$(g++ -std=c++17 -O2 -o ./build/a $filepath && ./build/a)
echo "$res"