# https://app.codesignal.com/arcade/code-arcade/well-of-integration/3QMXNwGfvLMoQwed7
def houseNumbersSum(values):
    result = 0
    # Add up the numbers of houses seen until seeing a 0 value.
    for value in values:
        if value == 0:
            break
        result += value

    # This will also sum all values until the first found 0.
    return sum(values[:values.index(0)])
