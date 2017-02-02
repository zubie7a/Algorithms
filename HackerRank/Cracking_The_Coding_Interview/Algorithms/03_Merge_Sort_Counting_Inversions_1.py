# https://www.hackerrank.com/challenges/ctci-merge-sort

# This is a headache-worthy way of doing it with indices.
def mergeSort(arr, l_index, r_index):
    # For [] or [x], return the same array, and 0 inversions.
    if l_index + 1 == r_index:
        return 0
    # Get the middle point of the current array.
    mid = (l_index + r_index) / 2
    k = (r_index - l_index)
    # Slice the array into two halves, then call a recursive mergeSort on each.
    countL = mergeSort(arr, l_index, mid)
    countR = mergeSort(arr, mid, r_index)
    inversions = 0
    res = [0 for _ in xrange(k)]
    i, j = 0, 0
    while (l_index + i < mid) and (mid + j < r_index): 
        # The left value goes in.
        if arr[l_index + i] <= arr[mid + j]:
            res[i + j] = arr[l_index + i]
            i += 1
        # The right value goes in.
        # Also this means an inversion occurred.
        elif arr[l_index + i] > arr[mid + j]:
            res[i + j] = arr[mid + j]
            j += 1
            # This value is an inversion of everything to the left.
            inversions += mid - l_index - i
    while l_index + i < mid:
        res[i + j] = arr[l_index + i]
        i += 1
    while mid + j < r_index:
        res[i + j] = arr[mid + j]
        j += 1
    for x in range(k):
        arr[l_index + x] = res[x]
    return inversions + countL + countR
    
n = int(raw_input())
for i in xrange(n):
    num = int(raw_input())
    arr = map(int, raw_input().split())
    # 0: left boundary.
    # num: right boundary.
    countInvs = mergeSort(arr, 0, num)
    print countInvs
