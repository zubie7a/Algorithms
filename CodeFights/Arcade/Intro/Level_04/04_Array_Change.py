# https://codefights.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
def arrayChange(inputArray):
    moves = 0
    # Minimum number of adds to make a sequence strictly increasing.
    for i in range(len(inputArray) - 1):
        cur, next = inputArray[i], inputArray[i+1]
        diff = 0
        if cur >= next:
            diff = cur - next + 1
        moves += diff
        inputArray[i+1] = next + diff
    return moves
