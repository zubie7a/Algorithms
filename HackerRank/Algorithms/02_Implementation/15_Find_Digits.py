# https://www.hackerrank.com/challenges/find-digits
t = int(raw_input())
# Check by how many of its digits (sans 0) can a number
# be divided evenly.
for _ in xrange(t):
    number, count = raw_input(), 0
    for digit in number:
        if int(digit) != 0:
            count += (int(number) % int(digit) == 0)
    print count
