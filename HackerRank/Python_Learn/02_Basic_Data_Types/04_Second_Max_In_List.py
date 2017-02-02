# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(raw_input())
    # Find the second max number in a list.
    arr = map(int, raw_input().split())
    st = set(arr) # O(n)
    st.discard(max(st)) # O(n)
    print max(st) # O(n)

# Or...
n = int(raw_input())
vals = map(int, raw_input().split(" "))
fst, snd = None, None
for i in range(n):
    if vals[i] > fst:
        snd = fst
        fst = vals[i]
    elif vals[i] > snd and vals[i] < fst:
        snd = vals[i]
print snd