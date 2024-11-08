"""This module defines a function that generates invitations."""

import os


def generate_invitations(template, attendees):
    """Generate invitation with a template."""
    if not isinstance(template, str):
        raise TypeError(f"Template have invalid type: {type(template)}")

    if not is_list_of_dict(attendees):
        raise TypeError(f"Attendees have invalid type: {type(attendees)}")

    # Delete the whitespaces and check if there is a string
    if not template.strip():
        raise ValueError("Template is empty, no output files generated.")

    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    # File incrementer
    i = 1
    try:
        for attendee in attendees:
            template_to_write = template
            for key, value in attendee.items():
                form_key = f"{{{key}}}"
                template_to_write = template_to_write.replace(
                    form_key, attendee.get(key) or "N/A"
                )

            while os.path.exists(f"output_{i}.txt"):
                print(f"output_{i}.txt already exists.")
                i += 1

            with open(f"output_{i}.txt", "x", encoding="utf-8") as f:
                f.write(template_to_write)
                print(f"output__{i}.txt created.")
            i += 1

    except Exception as e:
        print(f"output_{i}.txt could not be created : {e}")


def is_list_of_dict(attendees):
    """Check if the object is a list af dictionaries."""
    return isinstance(attendees, list) and all(
        isinstance(attendee, dict) for attendee in attendees
    )
