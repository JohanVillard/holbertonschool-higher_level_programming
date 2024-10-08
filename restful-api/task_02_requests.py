#!/usr/bin/python3
"""This module fetch, print and save post."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch and print posts."""
    # Stores all posts
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the code HTTP
    print(f"Status Code: {r.status_code}")

    # Check if code is ok (200)
    if r.ok:
        # Convert all posts in json format
        r_json = r.json()

        # Itere in each post and print the value of title key
        for post in r_json:
            print(f"{post['title']}")


def fetch_and_save_posts():
    """Fetch and save posts."""
    # Stores all posts
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.ok:
        # Convert all posts in json format
        r_json = r.json()

        new_list = []

        # Structure the data
        for post in r_json:
            new_list.append(
                {
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                 }
            )

        # Write data into CSV file
        with open("posts.csv", "w", newline="") as csv_f:
            # Store the columns
            field_names = ["id", "title", "body"]

            # Create a object to write structured dictionary in the csv file
            writer = csv.DictWriter(csv_f, fieldnames=field_names)

            # Write the header in the file corresponding to field_names string
            writer.writeheader()

            # Write row correspondind to field_name string
            writer.writerows(new_list)
