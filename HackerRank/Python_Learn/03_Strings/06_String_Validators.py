# https://www.hackerrank.com/challenges/string-validators
from __future__ import print_function
if __name__ == '__main__':
    s = raw_input()
    # There's string validators, but those apply to a whole string. Lets
    # use them over string chars to see if a string contains each kind
    # of character,
    alnum = any([x.isalnum() for x in s])
    alpha = any([x.isalpha() for x in s])
    digit = any([x.isdigit() for x in s])
    lower = any([x.islower() for x in s])
    upper = any([x.isupper() for x in s])
    print(*[alnum, alpha, digit, lower, upper], sep="\n")
