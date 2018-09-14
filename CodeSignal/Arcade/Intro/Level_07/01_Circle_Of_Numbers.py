# https://app.codesignal.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ
def circleOfNumbers(n, first_number):
    # In a circle of numbers from 0 to (n - 1), return the number
    # radially opposite to a given first number. Just add the half
    # of the total numbers but remember to wrap around with modulus.
    return (first_number + (n//2)) % n
