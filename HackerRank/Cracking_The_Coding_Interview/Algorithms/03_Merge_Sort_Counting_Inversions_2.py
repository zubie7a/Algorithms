# https://www.hackerrank.com/challenges/ctci-merge-sort

# This is a simpler way of doing it with slices.
def mergeSort(arr):
    # For [] or [x], return the same array, and 0 inversions.
    if len(arr) <= 1:
        return arr, 0
    # Get the middle point of the current array.
    mid = len(arr) / 2    
    # Slice the array into two halves, then call a recursive mergeSort on each.
    left, countL = mergeSort(arr[:mid])
    right, countR = mergeSort(arr[mid:])    
    res, inversions = [], 0
    i, j = 0, 0
    # Sentinel values at the end of the arrays, so that nothing will compare
    # to these as less.
    left += [1 << 31]
    right += [1 << 31]
    # We know that len(arr) elements have to be merged back.
    # One sentinel will be reached but not both. Once it has
    # arrived to the second one, it will exit loop.
    for _ in xrange(len(arr)):
        # Left value goes in, and if equal its not an inversion.
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        # Right value goes in, and its an inversion of everything in left.
        else:
            res.append(right[j])
            j += 1
            inversions += len(left) - i - 1
    # Doing this gives a time out. Better to use sentinel values.
    # res.extend(left[i:])
    # res.extend(right[j:])

    # Return the merged array, and the total inversions so far.
    return res, inversions + countL + countR
    
n = int(raw_input())
for i in xrange(n):
    a = int(raw_input())
    arr = map(int, raw_input().split())
    _, countInvs = mergeSort(arr)
    print countInvs