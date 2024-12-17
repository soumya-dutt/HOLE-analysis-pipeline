#!/bin/bash

# Check if a working directory is specified
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_working_directory>"
    exit 1
fi

# Assign the specified directory to a variable
WORKING_DIR="$1"

# Check if the specified directory exists
if [ ! -d "$WORKING_DIR" ]; then
    echo "The specified directory does not exist: $WORKING_DIR"
    exit 1
fi

# Loop through each subdirectory in the specified working directory
for dir in "$WORKING_DIR"/*/; do
    # Check if the directory contains a PDB file
    pdb_file=$(find "$dir" -maxdepth 1 -name "*.pdb")

    if [ -n "$pdb_file" ]; then
        echo "Processing directory: $dir"

        # Generate hole.inp file
        cat > "$dir/hole.inp" << EOF
COORD  *.pdb
RADIUS  ../../simple.rad
CPOINT  9.969740867614746 -1.0505282878875732 -8.498347282409668
CVECT   0.0 0.0 1.0
SPHPDB  hole.sph
CONN
CAPSULE
ENDRAD  10.0
EOF

        # Navigate to the subdirectory
        pushd "$dir" > /dev/null

        # Run the hole program
        hole < hole.inp > hole_out.txt

        # Return to the original directory
        popd > /dev/null
    else
        echo "No PDB file found in $dir, skipping."
    fi
done

echo "All done!"
