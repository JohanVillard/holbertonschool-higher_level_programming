"""This module defines a function that generates invitations."""

import logging
import os

with open("template.txt", "r") as f:
    template = f.read()


def generate_invitations(template, attendees):
    """Generate invitation."""
    if not isinstance(template, str):
        raise TypeError(f"Template have invalid type: {type(template)}")

    if not is_list_of_dict(attendees):
        raise TypeError(f"Attendees have invalid type: {type(attendees)}")

    if not template:
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

        # File incrementer
    i = 1
    for attendee in attendees:
        try:
            for key, value in attendee.items():
                template_to_write = template
                template_to_write = template_to_write.replace(
                    "{name}", attendee.get("name") or "N/A"
                )
                template_to_write = template_to_write.replace(
                    "{event_title}", attendee.get("event_title") or "N/A"
                )
                template_to_write = template_to_write.replace(
                    "{event_date}", attendee.get("event_date") or "N/A"
                )
                template_to_write = template_to_write.replace(
                    "{event_location}", attendee.get("event_location") or "N/A"
                )

            while os.path.exists(f"output_{i}.txt"):
                print(f"output_{i}.txt already exists.")
                i += 1

            try:
                with open(f"output_{i}.txt", "x", encoding="utf-8") as f:
                    f.write(template_to_write)
                    i += 1
            except Exception as e:
                logging.error(f"output_{i}.txt could not be created : {e}")
        except Exception as e:
            logging.error(e)


def is_list_of_dict(attendees):
    """Check if the object is a list af dictionaries."""
    return isinstance(attendees, list) and all(
        isinstance(attendee, dict) for attendee in attendees
    )
