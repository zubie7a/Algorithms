# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/ND8nghbndTNKPP4Tb
def firstReverseTry(arr):
    if len(arr) == 0:
        return arr
    # Reverse the first and last elements.
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
