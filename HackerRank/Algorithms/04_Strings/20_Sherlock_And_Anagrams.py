# https://www.hackerrank.com/challenges/sherlock-and-anagrams

def nCr(n, r):
    # To cancel the (n-r)! part of (n)! with the highest
    # value possible. (n)! / (n-r)! == (n)*(n-1)*(...)*(n-r+1)
    r = min(r, n-r)
    # nC1 or nCn is 1.
    if r == 0: return 1
    # nCr is...
    # (n)! / ((n-r)! * r!)
    # ((n)! / (n-r)!) * 1/r!
    # n*(n-1)*...(n-r+1)  * 1/r!
    num = reduce(lambda x, y: x*y, xrange(n, n-r, -1))
    den = reduce(lambda x, y: x*y, xrange(1, r+1))
    return num/den

from collections import Counter
t = int(raw_input())
for _ in xrange(t):
    s = raw_input()
    c = Counter()
    # Generate all possible substrings starting at each
    # character.
    for i in range(len(s)):
        word = s[i]
        # Add single char substring to the counter.
        c[word] += 1
        for j in range(i + 1, len(s)):
            word += s[j]
            # Add sorted substring to the counter.
            c["".join(sorted(word))] += 1
    # For values in the counter, if its greater or equal 
    # than 2, then the amount of anagramatic pairs is 
    # nCr(count, 2). The sum of all these will be the 
    # total of pairs.
    print sum([nCr(val, 2) for val in c.values() if val >= 2])
