"""This module defines a function that generates invitations."""

import os


def generate_invitations(template, attendees):
    """Generate invitation with a template."""
    if not isinstance(template, str):
        raise TypeError(f"Template have invalid type: {type(template)}")

    if not is_list_of_dict(attendees):
        raise TypeError(f"Attendees have invalid type: {type(attendees)}")

    if not template.strip():
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # File incrementer
    for index, attendee in enumerate(attendees, start=1):
        try:
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
            while os.path.exists(f"output_{index}.txt"):
                index += 1

            with open(f"output_{index}.txt", "w", encoding="utf-8") as f:
                f.write(template_to_write)
                print(f"output__{index}.txt created.")

        except Exception as e:
            print(f"output_{index}.txt could not be created : {e}")


def is_list_of_dict(attendees):
    """Check if the object is a list af dictionaries."""
    return isinstance(attendees, list) and all(
        isinstance(attendee, dict) for attendee in attendees
    )
