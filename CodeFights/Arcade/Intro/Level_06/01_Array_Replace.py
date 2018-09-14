# https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm
def arrayReplace(input_array, elem_to_replace, substitution_elem):
    # Given an array of integers, change all occurrences of an element to
    # replace with an element to substitute.
    # 
    # This function will be used in a `map` call to apply to every element.
    def replacer(x):
        return x if x != elem_to_replace else substitution_elem

    # Replace all elements of something in array with another thing,
    # using a function that will be applied to all elements.
    res = list(map(replacer, input_array))

    return res
