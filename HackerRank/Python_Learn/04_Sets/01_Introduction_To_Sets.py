# https://www.hackerrank.com/challenges/py-introduction-to-sets
def average(array):
    # Get the average of unique values.
    unique = set(array)
    return sum(unique)/len(unique)
