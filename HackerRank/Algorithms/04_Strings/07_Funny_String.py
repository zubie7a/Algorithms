# https://www.hackerrank.com/challenges/funny-string
t = int(raw_input())
# A string is funny if |s[i]-s[i-1]| == |r[i]-r[i-1]|
# for all i's where s is the string, and r its reverse.
# Also s[i] ~ r[i] are the ASCII values at position i.
for _ in xrange(t):
    s = map(lambda c: ord(c), raw_input())
    r = list(reversed(s))
    ls = len(s)
    absS = [abs(s[i] - s[i-1]) for i in range(ls)]
    absR = [abs(r[i] - r[i-1]) for i in range(ls)]
    funny = all([absS[i] == absR[i] for i in range(ls)])
    print "Not "*(not funny) + "Funny"
