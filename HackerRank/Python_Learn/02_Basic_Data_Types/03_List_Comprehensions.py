# https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    x, y, z, n = int(raw_input()), int(raw_input()), int(raw_input()), int(raw_input())
    x, y, z = x + 1, y + 1, z + 1
    # [ expression-involving-loop-vars for outer-loop-var in outer-sequence for inner-loop-var in inner-sequence ]
    # For X, Y and Z print 3D coordinates that don't add up to a value N.
    arr = [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i+j+k != n]
    print arr
