# https://www.hackerrank.com/challenges/kangaroo
x1, v1, x2, v2 = map(int, raw_input().split())
# There's two kangaroos, starting at position x1/x2
# and with speed v1/v2. Will they ever land on the
# same spot simultaneously?
xdiff = x2 - x1
vdiff = v2 - v1
positive = lambda x: x >= 0

# This means one started ahead of the other with higher
# speed, meaning the other one will never catch up :-(
if positive(xdiff) == positive(vdiff):
    print "NO"
else:
    # The difference of positions has to be evenly
    # divisible by the difference of the speeds.
    if xdiff % vdiff == 0:
        print "YES"
    else:
        print "NO"
