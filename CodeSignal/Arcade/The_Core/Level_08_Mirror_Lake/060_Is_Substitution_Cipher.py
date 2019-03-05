# https://app.codesignal.com/arcade/code-arcade/mirror-lake/rNrF4v5etMdFNKD3s
def isSubstitutionCipher(string1, string2):
    # Is one string able to be made with a substitution cipher?
    # We don't know what it is, but we can start comparing both
    # and inferring what a candidate substitution may be. Then,
    # this substitution has to hold on onwards for it to be valid.

    cipher = {}
    used = {}
    for i in range(len(string1)):
        char1, char2 = string1[i], string2[i]
        # Character found has not been substituted so far.
        if not(char1 in cipher):
            # But we have to find out if the characters that will
            # be used for substitution hasn't been used elsewhere.
            if char2 in used:
                return False
            cipher[char1] = char2
            used[char2] = 1
        # The cipher is not consistent with previous substitutions.
        elif cipher[char1] != char2:
            return False

    # The substitutions were consistent all along.
    return True
