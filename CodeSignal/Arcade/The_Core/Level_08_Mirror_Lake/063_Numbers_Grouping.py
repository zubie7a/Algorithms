# https://app.codesignal.com/arcade/code-arcade/mirror-lake/kGeuCkJNbqczCCqgg
def numbersGrouping(arr):
    groups = set([])
    for num in arr:
        group = (num - 1) // 10**4
        groups.add(group)
    # Each group will have a line as header and then all the numbers of that
    # group in separate lines, so total length will be amount of numbers and
    # the amount of headers.
    # n_lines = len(groups) + len(arr)

    # Building the set can also be done with a comprehension list.
    n_lines = len(set([(num - 1) // 10**4 for num in arr])) + len(arr)

    return n_lines
