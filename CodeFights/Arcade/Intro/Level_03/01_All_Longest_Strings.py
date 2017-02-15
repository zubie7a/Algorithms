# https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
def allLongestStrings(inArray):
    # Given an array of strings, return another containing only
    # the longest strings.
    lengths = [(len(str), str) for str in inArray]
    maxLen = max(lengths)
    # Filter only lengths of strings with same length as max.
    # These tuples will also contain the original string, in
    # the same originally occurring order.
    res = filter(lambda x: x[0] == maxLen[0], lengths)
    # Return just the string part of the filtered tuples.
    return list(map(lambda x: x[1], res))
