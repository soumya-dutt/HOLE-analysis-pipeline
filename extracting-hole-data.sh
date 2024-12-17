#!/bin/bash

# Main directory (change this to your directory path)
MAIN_DIR="37-48rep"

# Loop through each subdirectory
find "$MAIN_DIR" -mindepth 1 -maxdepth 1 -type d | while read -r subdir; do
    echo "Processing in directory: $subdir"
    # Check if 'hole_out.txt' exists in the subdirectory
    if [ -f "$subdir/hole_out.txt" ]; then
        egrep "mid-|sampled" "$subdir/hole_out.txt" | awk '{print $1, $2}' | sort -k1,1n > "$subdir/sorted-hole-data.txt"
        echo "Output saved to sorted-hole-data.txt in $subdir"
    else
        echo "hole_out.txt not found in $subdir"
    fi
done

