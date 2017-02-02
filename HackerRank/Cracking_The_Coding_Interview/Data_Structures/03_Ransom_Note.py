# https://www.hackerrank.com/challenges/ctci-ransom-note
from collections import Counter

m, n = map(int, raw_input().split())
magazine = raw_input().strip()
ransom = raw_input().strip()

# Create a count of words for the magazine, and the ransom note.
countMag = Counter(magazine.split())
countRan = Counter(ransom.split())

# For each word in the counter of ransom note words, check if the amount
# of that word in the ransom note is less than or equal than the count
# of that word in the magazine. Also, it is case sensitive.
if all([countRan[word] <= countMag[word] for word in countRan.keys()]):
    print "Yes"
else:
    print "No"
