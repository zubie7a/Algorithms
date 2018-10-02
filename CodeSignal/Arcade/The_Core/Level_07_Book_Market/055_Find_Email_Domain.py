# https://app.codesignal.com/arcade/code-arcade/book-market/TXFLopNcCNbJLQivP
def findEmailDomain(address):
    # Find the domain of a given email address, be careful
    # with @ signs previous to the actual one, the address
    # may not be valid but we still want the domain!
    parts = address.split("@")
    return parts[-1]
