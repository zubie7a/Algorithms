# https://www.hackerrank.com/challenges/camelcase
import re
# Get the count of words from a camelCase string.
string = raw_input()
# Using a RegEx
words = re.compile("[A-Z]").split(string)
print len(words)
# Or simply printing the uppercase characters' count  + 1
# print sum([char.isupper() for char in raw_input()]) + 1
