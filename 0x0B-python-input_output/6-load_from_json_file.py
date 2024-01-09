#!/usr/bin/python3
"""Creates objects"""
import json

def load_from_json_file(filename):
    """A creative function"""

    with open(filename) as f:
        return (json.load(f))
