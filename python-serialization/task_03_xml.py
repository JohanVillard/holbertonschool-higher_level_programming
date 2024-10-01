"""This module serialize/deserialize using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize the dictionary into XML.

    Parameters:
        dictionary (dict): The dictionary to convert into XML.
        filename (str): The filename to save the converted XML datas.
    """
    with open(filename, "wb") as f:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)

        tree.write(f)


def deserialize_from_xml(filename):
    """
    Deserialize XML data into a Python deserialized dictionary.

    Parameter:
        filename (str): The filename which contains the XML datas.

    Returns:
        dict: Thsi function returns a deserialized dictionary.
    """
    # Read the file
    # Get the xml tree
    tree = ET.parse(filename)
    # Get the root
    root = tree.getroot()

    new_dict = {}

    for child in root:
        new_dict[child.tag] = child.text

    return new_dict
