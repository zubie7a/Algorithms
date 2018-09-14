# https://app.codesignal.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW
def evenDigitsOnly(n):
    # Return if all digits on a number are even. For this convert the
    # number into a string so its individual digits can be itere
    return all([int(digit) % 2 == 0 for digit in str(n)])
