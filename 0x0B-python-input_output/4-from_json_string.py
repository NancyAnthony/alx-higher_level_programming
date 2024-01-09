#!/usr/bin/python3
"""JSON string 2 an obj"""

import json

def from_json_string(my_str):
    """Return a JSON represted obj"""

    return json.loads(my_str)
