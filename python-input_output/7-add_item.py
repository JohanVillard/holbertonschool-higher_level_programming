#!/usr/bin/python3
"""
This module defines a 'main' function that adds cmd-line arguments to a list.

Saves them to a JSON file, and loads the content back from the file.

This script follows these steps:
1. Retrieves arguments from the command line (excluding the script name).
2. Appends the arguments to a list.
3. Saves the list to a JSON file.
4. Loads the content from the JSON file.

Functions imported:
    load_from_json_file: Reads and parses a JSON object from a file.
    save_to_json_file: Saves a Python object as JSON to a file.

Execution:
    The script can be executed from the command line,
    passing any number of arguments.
    These arguments will be added to a list and stored in 'add_item.json'.

Usage example:
    $ ./script_name.py arg1 arg2 arg3
    This will save the list ['arg1', 'arg2', 'arg3'] to the file
    'add_item.json'.
"""

import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

if __name__ == "__main__":
    """
    Main function to handle command-line arguments,
    save them to a JSON file, and load the content back.
    """
    # Name a new file
    filename = "add_item.json"

    # Pass the command argument
    argv = sys.argv[1:]

    # Save argv list in a file
    save_to_json_file(argv, filename)

    # Load from json file
    load_from_json_file(filename)
