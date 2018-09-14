# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
def arrayChange(input_array):
    moves = 0
    # Minimum number of adds to make a sequence strictly increasing.
    for i in range(len(input_array) - 1):
        # Get current and next value.
        cur, next = input_array[i], input_array[i + 1]
        diff = 0
        # Store difference if current is greater, because then we
        # need to increment the next one to match current by the
        # difference and an extra move to satisfy the strictly
        # increasing condition.
        if cur > next:
            diff = cur - next + 1
        moves += diff
        # Update the original value, since now this change will affect
        # how it is compared with the value afterwards and so on. 
        input_array[i + 1] = next + diff

    return moves
