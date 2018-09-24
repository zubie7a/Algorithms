# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/H5PP5MXvYvWXxTytH
def rounders(n):
    # Turn a number into a number with only one non-zero digit using tail rounding.
    # If a digit is < 5, we round it to 0, if its >= 5, we round it to 10, which
    # still makes the digit 0 but carries one over. At the end it should be all
    # zeros except the leftmost possition.
    str_n = str(n)[::-1]
    result = ""
    carry = 0
    # Since the number has been reversed, we can iterate normally from left to right.
    for i in range(len(str_n)):
        digit = int(str_n[i])
        # Add the previous carry.
        digit = digit + carry
        # Reset the carry.
        carry = 0
        # Check that is not the last digit, round everything except it.
        if i + 1 < len(str_n):
            # Check if the digit with the carry so far has exceeded 10.
            if digit >= 5:
                carry = 1
            # Regardless of rounding up or down, all digits except the last will be
            # rounded to 0, but the rounded ups will create a carry over.
            digit = 0
        # The last digit is a special case, it should not be rounded. However,
        # if the last digit was 9 and there was a carry over, then the "digit"
        # would really be a 10, but will still be appended normally.
        result = ("{}".format(digit)) + result

    return int(result)
