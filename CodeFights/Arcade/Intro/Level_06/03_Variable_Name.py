# https://codefights.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
import re
def variableName(name):
    # Return if its a valid variable name.
    return bool(re.match("^[a-zA-Z_][a-zA-Z_0-9]*$", name))
