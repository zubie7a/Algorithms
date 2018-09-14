# https://app.codesignal.com/arcade/intro/level-5/veW5xJednTy4qcjso
def isIPv4Address(input_string):
    # Separate the octets value, in IPs xxx.xxx.xxx.xxx each 3 values
    # are 8 bits since they range from 0 to 255 (2^8 - 1).
    octets = input_string.split(".")
    # This is not an IP.
    if len(octets) != 4:
        return False
    # Try converting all octets to int and validate the range,
    # if any fail to convert (empty, or non numeric chars) it will
    # fail and then go to exception.
    try:
        return all([0 <= int(octet) <= 255 for octet in octets])
    except:
        return False
