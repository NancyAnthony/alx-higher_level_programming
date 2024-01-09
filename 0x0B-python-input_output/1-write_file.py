#!/usr/bin/python3
"""Function that writes to a file"""
def write_file(filename="", text=""):
    """
    This function writes a string to a text file
    it returns the number of written characters
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
