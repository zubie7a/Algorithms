# 02 - Trouble Sort

t = int(input())

for case in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    # Trouble sort is like bubble sort, but instead will compare pairs separated
    # away by two positions. This means that only elements in even positions will
    # be compared with other elements in even positions, and the same for odds.
    evens = []
    odds  = []
    for i in range(0, n):
        if (i % 2):
            odds.append(nums[i])
        else:
            evens.append(nums[i])
    # After having separated even and odd index elements, sort that list any
    # way you want. No matter how much Trouble Sort runs, it will only leave
    # sorted evens and odds in their positions. 
    evens.sort()
    odds.sort()
    final = []
    evens_iterator = 0
    odds_iterator  = 0
    for i in range(0, n):
        if (i % 2):
            final.append(odds[odds_iterator])
            odds_iterator += 1
        else:
            final.append(evens[evens_iterator])
            evens_iterator += 1
    pos = -1
    # After having been merged back, the first element thats not sorted is
    # where the sorting is broken, because Trouble Sort will never be able
    # to sort it properly.
    for i in range(1, n):
        if (final[i] < final[i - 1]):
            pos = i - 1
            break
    
    result = "Case #%d: " % (case)
    result += str(pos) if (pos != -1) else "OK"
    print(result)
