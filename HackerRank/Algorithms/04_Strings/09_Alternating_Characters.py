# https://www.hackerrank.com/challenges/alternating-characters
t = int(raw_input())
for _ in xrange(t):
    s, i = raw_input(), 1
    old = s
    while i < len(s):
        # If there's two repeated consecutive
        # characters, remove one of them by slicing the
        # string skipping i-1.
        if s[i] == s[i-1]:
            s = s[:i-1] + s[i:]
            # Reduce the iterator to adjust to the
            # length cut.
            i = max(0, i-1)
        i += 1
    print len(old) - len(s)
