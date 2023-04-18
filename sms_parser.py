#!/bin/python3

'''
Simple Google ADB message parser

Get data using (requires ADB but not root):
    adb shell content query --uri content://sms/inbox
'''

import sys

addr_txt = "address="
body_txt = "body="

if len(sys.argv) < 3:
    print("Invalid arguments")
    print("Example Usage:",sys.argv[0],"body", "address", "sms_file")
    sys.exit(1)

filename = sys.argv[-1]

print_address = 0
if "address" in sys.argv[:-1]:
    print_address = 1

print_body = 0
if "body" in sys.argv[:-1]:
    print_body = 1

def get_field(line, field):
    try:
        if field in line:
            field_index = line.index(field)
            next_comma  = line.index(",", field_index)
            field_data = line[field_index+len(field):next_comma]
            return field_data
    except ValueError:
        pass
    return None

with open(filename, "r", encoding="utf-16") as sms_file:
    for line in sms_file:
        
        address = get_field(line, addr_txt)
        body = get_field(line, body_txt)
        
        if address and print_address:
            print(address, end="|")

        if body and print_body:
            print(body, end="|")

        print()

