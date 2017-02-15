# https://codefights.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ
def circleOfNumbers(n, firstNumber):
    # In a circle of numbers from 0 to n-1, return the number
    # radially opposite to a given 'firstNumber
    return (firstNumber + n//2) % n
