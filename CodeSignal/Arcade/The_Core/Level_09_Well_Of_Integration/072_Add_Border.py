# https://app.codesignal.com/arcade/code-arcade/well-of-integration/ZCD7NQnED724bJtjN
def addBorder(picture):
    # Put a frame of "*" around a "picture" represented by a character matrix.
    rows = len(picture)
    cols = len(picture[0])
    result = ["*" * (cols + 2)]

    for row in picture:
        result.append("*" + row + "*")

    result.append("*" * (cols + 2))

    return result
