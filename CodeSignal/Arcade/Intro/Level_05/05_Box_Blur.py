# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP
def boxBlur(image):
    res = []
    '''
    To blur an image, take 3x3 squares, and average
    all their values into a single square. The resulting
    image will have less squares on each dimension because
    of the two vertical/horizontal squares lost when reducing
    3x3 grids to 1x1 grids.
    
    Input: image:
         [[36, 0,18, 9, 9,45,27], 
          [27, 0,54, 9, 0,63,90], 
          [81,63,72,45,18,27, 0], 
          [ 0, 0, 9,81,27,18,45], 
          [45,45,27,27,90,81,72], 
          [45,18, 9, 0, 9,18,45], 
          [27,81,36,63,63,72,81]]
   
    Output: boxBlur(image):
        [[39,30,26,25,31], 
         [34,37,35,32,32], 
         [38,41,44,46,42], 
         [22,24,31,39,45], 
         [37,34,36,47,59]]
    '''
    # Get the dimensions of the image.
    n, m = len(image), len(image[0])
    # Loop rows with inclusive limit of n - 3, not iterating
    # n - 2 and n - 1 because those will be lost while blurring.
    for i in range(n - 3 + 1):
        # Clean row to append to output image.
        row = []
        # Same boundary for the columns.
        for j in range(m - 3 + 1):
            average = 0
            # Iterate in a mini 3x3 grid at the current position
            # to find the average value.
            for x in range(3):
                for y in range(3):
                    average += image[i + x][j + y]
            # Round the value down since pixels are ints.
            average //= 9
            row.append(average)
        res.append(row)

    return res
