# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LbuWRHnMoJH9SAo4o
def magicalWell(a, b, n):
    # There's a well which has two initial values a and b. You throw a marble
    # into it, and you get a * b dollars and then both values increase by 1.
    # How much money will you make?
    # 0. (a + 0) * (b + 0)   n - n
    # 1. (a + 1) * (b + 1)   n - 2
    # 2. (a + 2) * (b + 2)   n - 1
    # 3. (a + n) * (b + n)   n 
    # return sum([ (a + i) * (b + i) for i in range(n)])
    
    # 1. a*b + 0*a + 0*b + 0*0
    # 2. a*b + 1*a + 1*b + 1*1
    # 3. a*b + 2*a + 2*b + 2*2
    # There will be n amount of (a * b)
    n_ab = n * (a * b)
    # 0*a + 1*a + 2*a + ... + (n - 1) * a == a * sum(i = (0 .. n - 1), i) 
    a_sum = a * (n * (n - 1)) / 2
    # 0*b + 1*b + 2*b + ... + (n - 1) * b == b * sum(i = (0 .. n - 1), i) 
    b_sum = b * (n * (n - 1)) / 2
    # 0*0 + 1*1 + 2*2 + ... + (n - 1)**2 == sum(i = (0 .. n - 1), i**2)
    isq_sum = (n - 1) * (n) * ((2 * (n - 1)) + 1) / 6

    return n_ab + a_sum + b_sum + isq_sum
