# https://codefights.com/interview/4e6LZSessGpKPx3uB
# String Reformatting: Google.
def stringReformatting(s, k):
    # Remove the dashes, invert the string, then create a new
    # string from the original one but putting a dash before
    # every k-th character. The last grouping could have less
    # than k characters and thats no problem.
    s = s.replace("-", "")[::-1]
    res = ["-"*(i % k == 0) + s[i] for i in range(len(s))]
    # Revert back the result.
    return "".join(res)[::-1][:-1]
