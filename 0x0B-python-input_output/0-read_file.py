#!/usr/bin/python3
"""Read file"""

def read_file(filename=""):
    """A read function"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
