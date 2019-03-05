# https://app.codesignal.com/arcade/code-arcade/mirror-lake/BsShkFDfbkWxozmMN
from collections import Counter

def createAnagram(s, t):
    # Given two strings `s` and `t`, find out how many replacements you
    # have to make in `s` to obtain an anagram of string `t`.
    return sum((Counter(t) - Counter(s)).values())
