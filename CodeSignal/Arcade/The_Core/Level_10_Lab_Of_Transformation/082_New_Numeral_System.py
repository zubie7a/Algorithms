# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/ngQTG9kra7GE9pnnK
def newNumeralSystem(az_digit):
    # The system effectively is a base-26 numeric system in which the letters
    # from A to Z are the az_digits.
    #
    # Create a mapping from a uppercase letter to its index.
    system = { i : chr(i + ord('A')) for i in range(ord('Z') - ord('A') + 1) }

    # We want to find which pair of other "az-digits" in the system can be added
    # up to the given "digit".
    idx_to_find = ord(az_digit) - ord('A')
    results = []

    # Do it until the middle to only a pair once, with the first lower than the
    # second, like "B + F" because "F + B" is a redundancy.
    for idx_1 in range(idx_to_find//2 + 1):
        idx_2 = idx_to_find - idx_1
        if idx_2 in system:
            chr_1 = system[idx_1]
            chr_2 = system[idx_2]
            results.append("{} + {}".format(chr_1, chr_2))

    return results
