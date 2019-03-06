# https://app.codesignal.com/arcade/code-arcade/well-of-integration/mJr7vgtN4X4ecL7ZA
import re

def timedReading(max_length, text):
    # Find all contiguous alphanumeric characters, these words have no hyphens.
    words = re.findall(r"[a-zA-Z]+", text)
    # Filter out words that have length greater than the max.
    words = list(filter(lambda word: len(word) <= max_length, words))
    # Return amount of words shorter than max length.
    return len(words)
