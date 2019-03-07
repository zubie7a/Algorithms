# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/dB9drnfWzpiWznESA/
def decipher(cipher):
    # A string is ciphered like this:
    # "easy" => ["e", "a", "s", "y"] => [101, 97, 115, 121] => 10197115121
    # Try to revert this process to go back from that number into the original
    # string with the assumption that all characters used were lowercase
    # alphabetical characters, so they are constrained between 97 and 124.
    # This prevents any ambiguity when doing the regex split.
    matches = list(re.findall(r"1[0-9]{2}|9[0-9]", cipher))
    convert = list(map(lambda x: chr(int(x)), matches))

    return "".join(convert)
