# https://codefights.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    def replacer(x):
        return x if x != elemToReplace else substitutionElem
    # Replace all elements of something in array with another thing.
    res = list(map(replacer, inputArray))
    return res
