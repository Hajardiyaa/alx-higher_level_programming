#!/usr/bin/python3
"""read_file fct"""
def read_file(filename=""):
    """""read the text file(UTF8) and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
