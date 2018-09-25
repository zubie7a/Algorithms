# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/mCkmbxdMsMTjBc3Bm
def arrayReplace(input_array, elem, subs):
    # Replace 'elem' by 'subs' in the input array.
    return [subs if x == elem else x for x in input_array]
