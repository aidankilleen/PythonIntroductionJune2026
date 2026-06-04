# find_largest_file.py

#!/usr/bin/env python3

import argparse
import os
import sys


def find_largest_file(start_folder):
    largest_file = None
    largest_size = -1

    for root, dirs, files in os.walk(start_folder):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                size = os.path.getsize(filepath)

                if size > largest_size:
                    largest_size = size
                    largest_file = filepath

            except (OSError, PermissionError):
                # Skip files that cannot be accessed
                continue

    return largest_file, largest_size


def main():
    parser = argparse.ArgumentParser(
        description="Recursively find the largest file in a folder."
    )

    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder to search (defaults to current folder)"
    )

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"Error: '{args.folder}' is not a valid folder.", file=sys.stderr)
        sys.exit(1)

    largest_file, largest_size = find_largest_file(args.folder)

    if largest_file is None:
        print("No files found.")
        sys.exit(0)

    filename = os.path.basename(largest_file)

    print(f"Filename: {filename}")
    print(f"Size: {largest_size} bytes")
    print(f"Path: {largest_file}")


if __name__ == "__main__":
    main()