# https://codefights.com/arcade/intro/level-6/6cmcmszJQr6GQzRwW
def evenDigitsOnly(n):
    # Return if all digits on a number are even.
    return all([int(digit) % 2 == 0 for digit in str(n)])
