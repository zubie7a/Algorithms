# https://app.codesignal.com/arcade/intro/level-10/TXFLopNcCNbJLQivP
def findEmailDomain(address):
    # Return the domain in a email address. Be careful because stray @
    # symbol may be inserted earlier so the domain is the stuff after
    # the last @ symbol found.
    return address.split("@")[-1]
