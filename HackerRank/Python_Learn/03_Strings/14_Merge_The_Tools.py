# https://www.hackerrank.com/challenges/merge-the-tools
from collections import OrderedDict
def merge_the_tools(s, k):
    # Input: AABCAAADA / 3
    # Output: AB / CA / AD
    iter = 0
    # Since s has length n, and k is a factor of n...
    n = len(s)
    # This will be repeated n/k times.
    while iter < n:
        # Create a substring t_i of length k.
        t_i = list(string[iter:iter + k])
        # Create an odict, to remove duplicates.
        od = OrderedDict.fromkeys(t_i)
        # Join the keys of the ordered dict to create u_i.
        print "".join(od.keys())
        # Increase the iterator by the k characters just consumed.
        iter += k
