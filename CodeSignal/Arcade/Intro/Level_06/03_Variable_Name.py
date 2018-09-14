# https://codefights.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
import re
def variableName(name):
    # Return if its a valid variable name. It should start with
    # an alphabetic character or with underscore, and then can be
    # followed by any alphanumeric characters and underscores.
    return bool(re.match("^[a-zA-Z_][a-zA-Z_0-9]*$", name))
