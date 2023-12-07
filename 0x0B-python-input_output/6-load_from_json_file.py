#!/usr/bin/python3
"""load_from_json_file fct"""
import json
def load_from_json_file(filename):
    """create an Object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
