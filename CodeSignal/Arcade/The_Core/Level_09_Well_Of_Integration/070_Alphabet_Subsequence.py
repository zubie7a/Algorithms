# https://app.codesignal.com/arcade/code-arcade/well-of-integration/Z9opBsx5fX6XfQJdt
def alphabetSubsequence(string):
    # Check if a string is a strictly increasing subsequence of the alphabet.
    # for idx_1 in range(len(string) - 1):
    #     idx_2 = idx_1 + 1
    #     if string[idx_1] >= string[idx_2]:
    #         return False

    # return True

    # Simpler Python using list comprehension to put booleans and a all() call
    # to check that all the booleans in the list are true.
    limit = len(string) - 1
    return all([string[i] < string[i + 1] for i in range(limit)])
