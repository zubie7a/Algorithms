# https://www.hackerrank.com/challenges/caesar-cipher-1
n, s, k = int(raw_input()), raw_input(), int(raw_input())

def rotK(char):
    base = "A"*char.isupper() + "a"*char.islower()
    # Char wasn't even alpha (not upper/lower)
    if base == "":
        return char
    # Convert the character to alphabet position.
    # ord() will give the ASCII number, so substract
    # the a/A (depending on case) ASCII value to get 
    # absolute index in alphabet.
    pos = ord(char) - ord(base)
    # Advance the position by k, then do mod 26.
    pos = (pos + k) % 26
    # Convert the new position back to character,
    # according to base (uppercase or lowercase).
    char = chr(pos + ord(base))
    return char

print "".join(map(rotK, s))
