# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/QrCSNQWhnQoaK9KgK
def arithmeticExpression(a, b, c):
    # Given an arithmetic expression a $ b = c, check if we can replace the $
    # operator with any other operator (e.g. +-*/) to make a valid expression.
    return (a + b == c) or (a - b == c) or (a / b == c) or (a * b == c)
