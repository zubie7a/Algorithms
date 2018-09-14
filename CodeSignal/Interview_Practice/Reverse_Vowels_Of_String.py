# https://codefights.com/interview/9JbYrEhK9tz6ANKLC
# Reverse Bowels of String: Google.
def reverseVowelsOfString(s):
    vowels = "aeiouAEIOU"
    # Filter just the vowels and reverse them.
    sv = list(filter(lambda x: x in vowels, s))[::-1]
    # Iterator to keep track of which reversed vowel
    # to put back into original string.
    iter = 0
    s = list(s)
    # Iterate over the original string,
    for i in range(len(s)):
        # If a vowel is found, overwrite it with the
        # current vowel from the filtered-and-reversed
        # list, and advance that list iterator.
        if s[i] in vowels:
            s[i] = sv[iter]
            iter += 1
    return "".join(s)
