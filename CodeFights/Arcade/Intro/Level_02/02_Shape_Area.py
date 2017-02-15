# https://codefights.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ
def shapeArea(n):
    '''                    _
              _          _| |_
     _      _| |_      _|     |_
    |_|    |_   _|    |_       _|
             |_|        |_   _|
                          |_|
    
    n=1      n=2          n=3
    
    
    Find the shape area for a given n.
    Starting with 1, each n gets an outer
    layer of a multiple of 4.
    n_1 =   1 + 4*0  = 1
    n_2 = n_1 + 4*1  = 5
    n_3 = n_2 + 4*2  = 13
    n_4 = n_3 + 4*3  = 25
    '''
    res = 1
    for i in range(n):
        res += 4*i
    return res
