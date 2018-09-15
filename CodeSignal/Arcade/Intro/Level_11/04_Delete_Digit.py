# https://app.codesignal.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX
def deleteDigit(n):
    # Convert the number to string...
    str_n = str(n)
    max_value = float('-inf')
    for i in range(len(str_n)):
        # Start trying the number without each digit, good thing is that once
        # its converted to string then doing slice operations on the string
        # to remove a character is easy and then can be converted back to int.
        new_value = int(str_n[:i] + str_n[i + 1:])
        # The maximum found value by removing one digit.
        max_value = max(max_value, new_value)

    return max_value
