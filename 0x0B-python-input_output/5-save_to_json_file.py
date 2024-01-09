#!/usr/bin/python3
"""Saves json file"""

import json

def save_to_json_file(my_obj, filename):
    """writes obj to a text fileo using JSON"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
