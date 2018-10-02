# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/MvX84CA5HN6GKqv7R
def squareDigitsSequence(a0):
    # Given a sequence of numbers a0, a1, a2, ... an, in which the next element
    # is the sum of the squares of the digits of the previous element, whats the
    # value of n when you find one element that already existed in the sequence?
    ax = a0
    # Set to keep track of existing values.
    seen_values = set([])
    while not (ax in seen_values):
        seen_values.add(ax)
        # Find the next value by adding up the squares of the digits of previous.
        ax = sum([int(digit) ** 2 for digit in str(ax)])

    # The amount of seen values + the last found element which already existed.
    return len(seen_values) + 1
