# https://codefights.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
def avoidObstacles(inputArray):
    n = len(inputArray)
    st = set(inputArray)
    # Minimal jump length to avoid all the obstacles.
    for i in range(1,42):
        j = i
        match = True
        while j <= 40:
            if j in st:
                match = False
                break
            j += i
        if match:
            return i
