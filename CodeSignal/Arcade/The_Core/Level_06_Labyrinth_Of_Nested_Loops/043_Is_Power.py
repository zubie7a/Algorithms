# https://app.codesignal.com/arcade/code-arcade/labyrinth-of-nested-loops/yBFfNv5fTqhcacZ7w
def isPower(n):
    # Check if a given value n is a power of another number.
    for i in range(0, n):
        for j in range(0, n + 1):
            if i**j == n:
                return True

    return False
