#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
f = open(filename, 'r')
if f == None:
    f = save_to_json_file([], filename)
print(my_list)
print(type(my_list))
