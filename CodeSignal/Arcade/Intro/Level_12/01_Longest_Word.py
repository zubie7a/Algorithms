# https://app.codesignal.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma
import re

def longestWord(text):
    # A word is english alphabetic characters together, no symbols.
    word = r'[A-Za-z]+'
    longest = ""
    # Find the longest word in a text.
    for match in re.finditer(word, text):
        string = match.group(0)
        if len(string) > len(longest):
            longest = string

    return longest
