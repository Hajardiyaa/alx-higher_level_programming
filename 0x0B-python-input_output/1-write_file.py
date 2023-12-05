#!/usr/bin/python3
"""write_file fct"""
def write_file(filename="", text=""):
    """returning the number of characters written from text to filenmae"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
