#!/usr/bin/python3
""""Function that appends a file"""
def append_write(filename ="", text=""):
    """
    Function that appends a string at the end of a text file
    It returns the no of characters added
    """
    with open(filename, "a", encoding"utf=8") as f:
        return f.write(text)
