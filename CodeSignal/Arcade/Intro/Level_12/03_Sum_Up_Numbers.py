# https://app.codesignal.com/arcade/intro/level-12/YqZwMJguZBY7Hz84T/solutions
import re

def sumUpNumbers(input_string):
    # From a receipt of amounts of items, extract the values
    # and add them up to find out how many items were purchased.
    number = r'[0-9]+'
    total = 0
    # for match in re.finditer(number, input_string):
    #    total += int(match.group(0))
    numbers = map(int, re.findall(number, input_string))
    total = sum(numbers)
    return total
