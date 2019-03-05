# https://app.codesignal.com/arcade/intro/level-12/sCpwzJCyBy2tDSxKW
import re

def messageFromBinaryCode(code):
    # Take a message from a binary string and convert it into a human
    # readable ascii string!
    octet = r'[01]{8}'
    result = ""
    for match in re.finditer(octet, code):
        bin_value = match.group(0)
        ascii_pos = int(bin_value, 2)
        ascii_val = chr(ascii_pos)
        result += ascii_val

    return result
