#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Execute a function safely."""
    try:
        return fct(*args)  # Exécute la fonction avec les arguments fournis
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
