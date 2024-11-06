import logging
import os

with open("template.txt", "r") as f:
    src = f.read()


def generate_invitations(template, attendees):
    """Generate invitation."""
    try:
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
            for key, value in attendee.items():
                if value is None:
                    attendee[key] = "N/A"

            template_to_write = template
            for key, value in attendee.items():
                key_sans_accolade = f"{{{key}}}"
                template_to_write = template_to_write.replace(key_sans_accolade, value)

            if os.path.exists(f"output_{i}.txt"):
                i += 1
                continue

            with open(f"output_{i}.txt", "w") as f:
                f.write(template_to_write)
            i += 1
    except Exception as e:
        logging.error(e)


def is_list_of_dict(attendees):
    """Check if the object is a list af dictionaries."""
    return isinstance(attendees, list) and all(
        isinstance(attendee, dict) for attendee in attendees
    )
