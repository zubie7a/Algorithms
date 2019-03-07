# https://app.codesignal.com/arcade/code-arcade/lab-of-transformations/QKnGhkoi4wKr6xY9b
def characterParity(symbol):
    if symbol.isdigit():
        return "odd" if int(symbol) % 2 == 1 else "even"
    else:
        return "not a digit"
