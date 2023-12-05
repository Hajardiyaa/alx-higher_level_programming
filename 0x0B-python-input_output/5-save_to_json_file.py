#!/usr/bin/python3
"""save_to_json_file fct"""
import json
def save_to_json_file(my_obj, filename):
    """write an Object using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
