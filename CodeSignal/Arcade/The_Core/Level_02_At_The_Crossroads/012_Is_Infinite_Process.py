# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/aFF9HDm2Rsti9j5kc
def isInfiniteProcess(a, b):
    # Given integers a and b, determine whether the following pseudocode results
    # in an infinite loop or not:
    '''
        while a is not equal to b do
            increase a by 1
            decrease b by 1
    '''

    # The loop will be infinite if the starting position of a is higher than b,
    # but also if they are not both even or both odd because both imply they
    # can never meet when changing one position at a time.
    return (a > b) or ((a % 2) != (b % 2))
