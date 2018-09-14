# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def adjacentElementsProduct(input_array):
    max_prod = float('-inf')
    # Find the pair of adjacent elements with largest product.
    for i in range(1, len(input_array)):
        # Input array will contain at least two elements.
        max_prod = max(input_array[i] * input_array[i - 1] , max_prod)

    return max_prod
