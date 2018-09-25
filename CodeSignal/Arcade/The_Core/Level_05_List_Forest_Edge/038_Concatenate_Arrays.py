# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/GeqSK26bvdrarkGH9 
def concatenateArrays(a, b):
    # a += b
    # a.extend(b) : this takes all elements of b and puts them in a. If
    # you only did append, you'd append the whole b as a single element.
    # This does not return an array, it modifies the source one.
    a.extend(b)
    return a
