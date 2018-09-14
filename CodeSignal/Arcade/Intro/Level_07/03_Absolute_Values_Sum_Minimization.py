# https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq
def absoluteValuesSumMinimization(A):
    # Given a sorted array of integers A, find such an integer x
    # that the value of:
    # abs(A[0] - x) + abs(A[1] - x) + ... + abs(A[A.length - 1] - x)
    # is the smallest possible.
    return A[len(A)//2 + len(A)%2 - 1]
    # tf = (float('inf'), float('inf')) 
    # for i in range(len(A)):
    #     s = sum([abs(A[k] - A[i]) for k in range(len(A))])
    #     tf = min([tf, (s, A[i])])
    # return tf[1]
