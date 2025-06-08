#!/bin/bash

# Check argument count
if [ "$#" -lt 4 ]; then
    echo "Usage: $0 ./file1.cpp ./file2.cpp ./generator.cpp n"
    exit 1
fi

# Assign arguments
FILE1=$1
FILE2=$2
GENERATOR=$3
N=${!#}  # Last argument

# Create build directory
mkdir -p ./build/test

# Compile all source files
if ! g++ "$FILE1" -o ./build/test/file1; then
    echo "Compilation failed for $FILE1"
    exit 1
fi

if ! g++ "$FILE2" -o ./build/test/file2; then
    echo "Compilation failed for $FILE2"
    exit 1
fi

if ! g++ "$GENERATOR" -o ./build/test/generator; then
    echo "Compilation failed for $GENERATOR"
    exit 1
fi

# Run test n times
for ((i = 1; i <= N; i++)); do
    # Generate input
    INPUT=$(./build/test/generator)

    # Get output from file1 and file2
    OUTPUT1=$(echo "$INPUT" | ./build/test/file1)
    OUTPUT2=$(echo "$INPUT" | ./build/test/file2)

    if [ "$OUTPUT1" != "$OUTPUT2" ]; then
        echo "Test failed at iteration $i"
        echo "Input:"; echo "$INPUT"
        echo "Output from file1:"; echo "$OUTPUT1"
        echo "Output from file2:"; echo "$OUTPUT2"
        exit 1
    fi

done

echo "All $N tests passed successfully."
