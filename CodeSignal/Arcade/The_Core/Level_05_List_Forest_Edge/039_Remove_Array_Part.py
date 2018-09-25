# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/vPJB7T28fyCeh2Ljn
def removeArrayPart(arr, l, r):
    # Remove the part of the array contained between l and r (inclusive).
    return arr[:l] + arr[r + 1:]
