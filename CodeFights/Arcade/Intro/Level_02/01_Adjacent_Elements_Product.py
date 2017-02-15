# https://codefights.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def adjacentElementsProduct(inputArray):
    maxProd = float('-inf')
    # Find the pair of adjacent elements with largest product.
    for i in range(1, len(inputArray)):
        maxProd = max(inputArray[i]*inputArray[i-1], maxProd)
    return maxProd
