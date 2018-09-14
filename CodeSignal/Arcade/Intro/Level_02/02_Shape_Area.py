# https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ
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
    n_1 =   1 + 4*0 = 1
    n_2 = n_1 + 4*1 = 5
    n_3 = n_2 + 4*2 = 13
    n_4 = n_3 + 4*3 = 25
    '''

    # res = 1
    # for i in range(n):
    #    res += (4 * i)

    '''
      We can use a formula too. 1 is the base area.
      Then each iteration adds an increasing number * 4.
      Without 4 factor, we get 1 + 2 + 3 + ... + (n - 1).
      So 1 + 4 * (sum of values from 1 to (n - 1)).
      And the formula for such sum of values is:
          (n * (n - 1) / 2
    '''
    res = 1 + (4 * (n * (n - 1) / 2))
    return res
