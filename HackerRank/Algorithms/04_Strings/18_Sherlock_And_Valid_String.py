# https://www.hackerrank.com/challenges/sherlock-and-valid-string
from collections import Counter
counts = Counter(raw_input())
# This is the char : count with less number of occurrences.
minReduce = lambda x,y: x if x[1] <= y[1] else y
minItem = reduce(minReduce, counts.items())
# Get the items with this same number of occurrences.
minFilter = lambda x: x[1] == minItem[1]
minItems = filter(minFilter, counts.items())
# This is the char : count with most number of occurrences.
maxReduce = lambda x,y: x if x[1] >= y[1] else y
maxItem = reduce(maxReduce, counts.items())
# Get the items with this same number of occurrences.
maxFilter = lambda x: x[1] == maxItem[1]
maxItems = filter(maxFilter, counts.items())

# If n-1 elements are min, and one max has to be changed.
changeMax = len(minItems) + 1 == len(counts.items())
# If n-1 elements are max, and one min has to be changed.
changeMin = len(maxItems) + 1 == len(counts.items())
# If all elements are identical.
allEqual = len(minItems) == len(counts.items())
# The difference is at most 1, needed when changing max
# element, because it has to be reduced by at most 1.
diffMax = (maxItem[1] - minItem[1]) <= 1
# The difference is at most 1, or the min element is
# 1, so that either the min element can be increased
# by 1 to match, or it can be decreased by 1 to be
# erased completely.
diffMin = diffMax or minItem[1] == 1

if any([changeMax and diffMax, changeMin and diffMin, allEqual]):
    print "YES"
else:
    print "NO"
