# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/KLbRMcWhaZi3dvYH5
import re

def increaseNumberRoundness(n):
    # Find the first non-zero value from right, and check if there's a
    # zero value before it so it can be swapped.
    # First revert the string.
    str_n = str(n)[::-1]
    i = 0
    # Now that it's reversed lets find the last 0 "from the right".
    while i < len(str_n) and str_n[i] == "0":
        i += 1
    # Now lets get a substring until the first non-zero character.
    new_n = str_n[i:]

    # See if there's any more zeros before the first non-zero, meaning
    # they can be swapped with the non-zero to make the number more round.
    # return new_n.find("0") != -1

    # Check if value has some non-zero digit, with any amount of 0s to its
    # right, and then any amount of digits to its left but at least one 0. 
    return len(re.findall(r'^[0-9]*0[0-9]*[^0][0]*', str(n)))
