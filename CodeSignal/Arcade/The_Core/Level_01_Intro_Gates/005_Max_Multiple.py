# https://app.codesignal.com/arcade/code-arcade/intro-gates/HEsmEacHr2s9wahjr
def maxMultiple(divisor, bound):
    # Given a divisor and a bound, find the largest integer N such that:
    #     * N is divisible by divisor.
    #     * N is less than or equal to bound.
    #     * N is greater than 0.
    # It is guaranteed that such number exists.
    # 
    # The limit is bound, so do integer division with the divisor and then multiply
    # it back with divisor to see which is the closest number to bound that can
    # be divided by divisor.
    return bound//divisor * divisor
