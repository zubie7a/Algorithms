# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/JeDDnToFtitiiWDZn
def cipher26(message):
    # A message was encrypted using the following cipher:
    # Every letter a-z has a value 0-26.
    # The i-th letter number is the sum of all previous letter numbers % 26.
    # Because of this, every letter on the cipher depends on the previous one.
    # How do we find the original message? This should be called 'decipher'.
    prev_number = 0
    result = ""

    # For cipher26(message) = output, it should be so that:
    # message = "taiaiaertkixquxjnfxxdh",
    # output  = "thisisencryptedmessage".
    #
    # letter 0: t -> 19 -> t;
    # letter 1: th -> (19 + 7) % 26 -> 0 -> a;
    # letter 2: thi -> (19 + 7 + 8) % 26 -> 8 -> i;
    # ...etc

    for char in message:
        # Find what was needed to be added to the previous character number
        # to get the value of the current ciphered character. Add 26 to the
        # current number so that we can substract the previous one safely.
        cur_number = ord(char) - ord('a') + 26
        # After substracting the previous one, just do modulus 26 again.
        orig_char = chr((cur_number - prev_number) % 26 + ord('a'))
        # After finding the original character, keep appending it to result.
        result += orig_char
        # Keep storing only the previous character number.
        prev_number = ord(char) - ord('a')

    return result
