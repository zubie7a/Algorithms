# https://codefights.com/arcade/intro/level-5/veW5xJednTy4qcjso
def isIPv4Address(inputString):
    octets = inputString.split(".")
    if len(octets) != 4:
        return False
    try:
        return all([0 <= int(oc) <= 255 for oc in octets])
    except:
        return False
