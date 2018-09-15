# https://app.codesignal.com/arcade/intro/level-12/NJJhENpgheFRQbPRA
def digitsProduct(product):
    # Find whats the minimum integer in order to reach a given 'product'
    # by multiplying all its digits, so the 'product' must divide completely
    # by all the digits of the source number until reaching 1.

    # The two corner cases, product 0 and product 1.
    # Product 0 is only achievable with 10.
    if product == 0:
        return 10
    # Product 1 is only achievable with 1.
    if product == 1:
        return 1

    res = ""
    # For all other products, start trying to divide by large numbers
    # at the least significant digits and then move to smaller numbers
    # at the most significat digits to try to minimize the source number.
    # The idea is that the digits of the source number multiplied should
    # give the product as a result, so their order doesn't matter and we
    # can purposefully put the larger numbers at the end. Also, 1s and 0s
    # are useless because 1s doesn't change the product, and 0s erase it.
    # Try with all digits from 9 to 2 decreasingly.
    for i in range(9, 1, -1):
        while True:
            # Keep dividing the number as much as possible and adding the
            # number to the result at its front.
            if product % i == 0:
                res = str(i) + res
                product /= i
            # Once you can't divide by this number anymore, exit.
            else:
                break

    num = -1
    # For the condition to be satisfied, the product must have been divided
    # entirely and there has to be something in the resulting string. An
    # initial product could've been divided up to certain point but if its
    # not divided completely then it can't be done.
    if len(res) != 0 and product == 1:
        num = int(res)

    return num
