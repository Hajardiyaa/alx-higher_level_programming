#!/usr/bin/python3
"""append_write"""
def append_write(filename="", text=""):
    """returning the number of characters appended from text to filename"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
