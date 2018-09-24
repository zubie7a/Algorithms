# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/scG8AFsPuqQGx8Qjf
def appleBoxes(k):
    # You have k square boxes, their space is:
    # 1x1, 2x2, 3x3 ... all the way up to kxk.
    # Boxes with odd size contain only yellow apples, boxes with even size
    # contain only red apples. What is the difference between red and yellow
    # apples in all boxes?
    # return sum([(i * i) * (-1 if (i % 2) else 1) for i in range(1, k + 1)])
    total = 0
    for i in range(1, k + 1):
        if i % 2 == 1:
            total += -(i * i)
        else:
            total += (i * i)

    return total
