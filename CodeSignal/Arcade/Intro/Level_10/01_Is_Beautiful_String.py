# https://app.codesignal.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE
from collections import Counter
import string

def isBeautifulString(input_string):
    # Lets create a base counter with all the letters of the alphabet,
    # then we add the actual counts. Without this, we can't account for
    # missing letters in the input string counts.
    # all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters = string.ascii_lowercase
    alphabet = Counter(all_letters)
    counts = Counter(input_string)
    counts = counts + alphabet
    sorted_keys = sorted(counts.keys())
    for index in range(len(sorted_keys) - 1):
        key1 = sorted_keys[index]
        key2 = sorted_keys[index + 1]
        if counts[key2] > counts[key1]:
            return False

    return True
