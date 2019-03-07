# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/vsKRjYKv4SCjzJc8r/
def higherVersion(ver1, ver2):
    # Split by dots, convert individual elements to ints.
    ver1 = [int(x) for x in ver1.split(".")]
    ver2 = [int(x) for x in ver2.split(".")]

    # This will do a comparison item-wise of all elements in the iterable arrays.
    return ver1 > ver2
