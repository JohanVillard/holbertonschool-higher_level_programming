"""This module converts CSV to JSON format."""

import csv
import json
import os


def convert_csv_to_json(filename):
    """
    Convert csv to JSON.

    Parameter:
        filename (str): The name of the CSV file to convert.
    """
    data = []

    # Check if file exist
    if not os.path.exists(filename):
        print("file not found")
        return False

    # Convert csv data into dictionary
    with open(filename, encoding="utf-8") as f_csv:
        # Check if file exists
        try:
            # Convert row in dictionary
            csv_reader = csv.DictReader(f_csv)

            # Add to a list
            for row in csv_reader:
                data.append(row)

        except TypeError:
            print("file not found")
            return False

    # Write the serialized json
    with open("data.json", "w", encoding="utf-8") as f_json:
        # Check if list is valid for conversion
        try:
            # Serialize the list of dictionaries into JSON
            f_json.write(json.dumps(data, indent=4))
            return True

        except TypeError:
            print("file not found")
            return False
