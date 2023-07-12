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

mv_dry() {
    # Function for dry running the mv command
    # !!! only works with 2 arguments atm !!!
    # !!! This doesn't support the -t flag !!!

    # check number of arguments
    if [ $# -ne 2   ]; then
        echo "<<< ERROR: must have 2 arguments , but $# given "
        return 1
    fi

    # check if source item exist
    if ! readlink -e "$1" > /dev/null; then
        echo "<<< ERROR: " "$item" " doesn't exist"
        return 1
    fi

    # check where file goes
    if [ -d "$2"  ]; then
        echo "Moving " "$1" " into " "$2" " directory"
    else
        echo "Renaming "  "$1" " to " "$2"
    fi
}