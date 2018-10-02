# https://app.codesignal.com/arcade/code-arcade/book-market/HJ2thsvjL25iCvvdm
import re

def isMAC48Address(input_string):
    # Check if a given string is a valid MAC 48 address.

    groups = input_string.split('-')
    if len(groups) != 6 or len(input_string) != 17:
        return False

    def valid_hex(group):
        return len(re.findall(r'[0-9A-F]{2}', group)) == 1

    valid = all([valid_hex(group) for group in groups])
    return valid
