# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
def avoidObstacles(input_array):
    # Array contains coordinates of obstacles located in straight line.
    st = set(input_array)
    max_value = max(input_array)
    # Find the minimal jump length to avoid all the obstacles.
    for i in range(1, max_value * 2):
        j = i
        match = True
        while j <= max_value:
            # If landed in an obstacle, stop trying.
            if j in st:
                match = False
                break
            j += i
        # If survived without landing on any obstacle, this is the
        # ideal jump length.
        if match:
            return i
