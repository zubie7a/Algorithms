# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/dB9drnfWzpiWznESA/
def alphanumericLess(s1, s2):
    tokens_1 = list(re.findall(r"[0-9]+|[a-z]", s1))
    tokens_2 = list(re.findall(r"[0-9]+|[a-z]", s2))
    idx = 0
    # Tie breakers, if all compared values are the same then the first
    # differing amount of leading zeros in a number will resolve it.
    t_1_zeros = 0
    t_2_zeros = 0
    while idx < len(tokens_1) and idx < len(tokens_2):
        token_1, token_2 = tokens_1[idx], tokens_2[idx]
        # If both are numeric
        if token_1.isdigit() and token_2.isdigit():
            if int(token_1) < int(token_2):
                return True
            if int(token_1) > int(token_2):
                return False
            if t_1_zeros == 0 and t_2_zeros == 0:
                # Store leading zeros but preserving only the first
                # found. Whenever anything is stored there will stop
                # storing new leading zeros.
                t_1_zeros = sum([x == "0" for x in token_1])
                t_2_zeros = sum([x == "0" for x in token_2])
        # If both are string
        elif token_1.isalpha() and token_2.isalpha():
            if token_1 < token_2:
                return True
            if token_1 > token_2:
                return False
        # If both are mixed...
        elif token_1 != token_2:
            # In mixed comparisson, digits come before letters.
            return token_1 < token_2

        idx += 1

    # If it was practically equal, return the one with the most
    # leading zeros as being "less".
    if t_1_zeros != 0 or t_2_zeros != 0:
        return t_1_zeros > t_2_zeros

    # If the leading zeros were equal too, then check if the first
    # string was the one completely exhausted to reach this point.
    # If both are equal then the first one is not strictly less.
    first_is_less = idx < len(tokens_2)

    return first_is_less
