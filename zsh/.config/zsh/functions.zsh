#!/bin/sh


# Function to recursively rename files and directories to lowercase
# Usage: rename_lower <directory>
rename_lower() {
    # Retrieve the directory path from the first argument
    local directory="${1:-$(pwd)}"

    # Loop through the files and directories in the given directory
    for SRC in $(find "$directory" -depth); do
        DST=$(dirname "$SRC")/$(basename "$SRC" | tr '[:upper:]' '[:lower:]')

        # Check if renaming is required
        if [ "$SRC" != "$DST" ]; then
            # Perform the renaming
            if [ ! -e "$DST" ]; then
                mv -T "$SRC" "$DST"
            else
                echo "$SRC was not renamed"
            fi
        fi
    done
}