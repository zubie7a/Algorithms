# https://app.codesignal.com/arcade/code-arcade/book-market/Ky2mjgmxnWLi6KNPp
def isUnstablePair(filename1, filename2):
    # Check if the sorting of the filenames depend on their casing or if
    # regardless of case the order will be the same.
    return ((filename1 < filename2 and filename1.lower() > filename2.lower())
        or (filename1 > filename2 and filename1.lower() < filename2.lower()))
