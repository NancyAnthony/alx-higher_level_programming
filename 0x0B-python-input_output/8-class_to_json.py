#!/usr/bin/python3
"""Function classs"""

def class_to_json(obj):
    """Obj Returner"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
        return res
