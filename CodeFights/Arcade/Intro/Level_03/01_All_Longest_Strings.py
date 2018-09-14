# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
def allLongestStrings(in_array):
    # Given an array of strings, return another containing only
    # the longest strings (all strings with longest length equal).
    lengths = [(len(str), str) for str in in_array]
    max_len = max(lengths)
    # Filter only lengths of strings with same length as max.
    # These tuples will also contain the original string, in
    # the same originally occurring order.
    res = filter(lambda x: x[0] == max_len[0], lengths)

    # Return just the string part of the filtered tuples.
    return list(map(lambda x: x[1], res))
