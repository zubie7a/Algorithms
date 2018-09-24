# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/xzeZqCQjpfDJuN72S
def additionWithoutCarrying(param1, param2):
    # Add the values of each column of each number without carrying.
    # Order them smaller and larger value.
    param1, param2 = sorted([param1, param2])
    # Convert both values to strings.
    str1, str2 = str(param1), str(param2)
    # Pad the smaller value with 0s so all columns have a match.
    str1 = "0" * (len(str2) - len(str1)) + str1

    res = ""
    for i in range(len(str2)):
        # Add up the integer value of each column, extract units with modulus,
        # then convert back to string and create a result string.
        res += str((int(str1[i]) + int(str2[i])) % 10)

    return int(res)
