import os


def generate_invitations(template, attendees):
    """Check the type of input"""
    # ============================Conditions================================ #

    if not isinstance(template, str):
        print("Error: The template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # ====================================================================== #

    for index, attendee in enumerate(attendees, start=1):
        try:
            invitation = template
            invitation = invitation.replace("{name}", attendee.get("name") or "N/A")
            invitation = invitation.replace(
                "{event_title}", attendee.get("event_title") or "N/A"
            )
            invitation = invitation.replace(
                "{event_date}", attendee.get("event_date") or "N/A"
            )
            invitation = invitation.replace(
                "{event_location}", attendee.get("event_location") or "N/A"
            )

            output_filename = f"output_{index}.txt"

            if os.path.exists(output_filename):
                print(
                    f"The file '{output_filename}' already exist, "
                    "it will not be overwritten"
                )
                continue

            with open(output_filename, "w") as file:
                file.write(invitation)
                print(f"Invitation successfully written to " f"'{output_filename}'.")

        except Exception as e:
            print(
                f"Error: An error occurred while generating "
                f"'{output_filename}': {e}"
            )
