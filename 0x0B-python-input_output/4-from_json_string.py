#!/usr/bin/python3
"""from_json_string fct"""
import json
def from_json_string(my_str):
    """returning the object represented by JSON string"""
    return json.loads(my_str)
