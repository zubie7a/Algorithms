# https://app.codesignal.com/company-challenges/verkada/GCykhwZcTrusPZfeQ
def blurFaces(img):
    h = len(img)
    w = len(img[0])
    # Blur each of the image's pixels with the average of the values
    # of the surrounding 8 positions excluding the value of the pixel
    # itself. Also if it's close to a boundary then use just the
    # available values.
    result = []
    # The possible deltas (horizontally or vertically).
    arr = [-1, 0, 1]
    for i in range(h):
        row = []
        for j in range(w):
            avg = 0
            cells = 0
            for di in arr:
                for dj in arr:
                    # Exceeded vertical bounds.
                    if di + i < 0 or di + i >= h:
                        continue
                    # Exceeded horizontal bounds.
                    if dj + j < 0 or dj + j >= w:
                        continue
                    # The very same position.
                    if di == 0 and dj == 0:
                        continue
                    avg += img[di + i][dj + j]
                    cells += 1
            avg /= cells
            row.append(avg)
        result.append(row)

    return result
