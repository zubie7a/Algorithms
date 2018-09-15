# https://app.codesignal.com/arcade/code-arcade/intro-gates/DdNKFA3XCX6XN7bNz
def candies(n, m):
    # n children have m candies, whats the max number of candies that can
    # be eaten considered all children have to eat exactly the same candies
    # and no candies can be split.
    return m//n * n
