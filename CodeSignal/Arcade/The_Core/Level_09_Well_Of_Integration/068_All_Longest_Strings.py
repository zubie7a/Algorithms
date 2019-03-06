# https://app.codesignal.com/arcade/code-arcade/well-of-integration/fzsCQGYbxaEcTr2bL
def allLongestStrings(strings):
    # Return the strings that have the maximum length in the original order
    # they appeared in the input array.
    max_len = max([len(string) for string in strings])
    # longest = list(filter(lambda string: len(string) == max_len, strings))
    # Instead of using a filter can also use a comprehension list with a condition.
    longest = [string for string in strings if len(string) == max_len]
    return longest
