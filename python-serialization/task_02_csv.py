"""This module converts CSV to JSON format."""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert csv to JSON.

    Parameter:
        filename (str): The name of the CSV file to convert.
    """
    data = []
    # Convert csv data into dictionary
    with open(filename, encoding="utf-8") as f_csv:
        # Check if file exists
        try:
            csv_reader = csv.DictReader(f_csv)

            for rows in csv_reader:
                data.append(rows)
        except TypeError:
            print("file not found")
            return False

    # Write the serialized json
    with open("data.json", "w", encoding="utf-8") as f_json:
        # Check if conversion valid
        try:
            # Serialize the list of dictionaries into JSON
            f_json.write(json.dumps(data, indent=4))
            return True
        except TypeError:
            print("file not found")
            return False
