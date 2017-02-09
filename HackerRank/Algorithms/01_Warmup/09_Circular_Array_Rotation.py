# https://www.hackerrank.com/challenges/circular-array-rotation
# For a list of n numbers, with k rotations to the right,
# and q queries for array positions after the list is rotated...
n, k, q = map(int, raw_input().split())
nums = map(int, raw_input().split())
# Print the number at the position of each query done.
for _ in range(q):
    query = int(raw_input())
    # But don't rotate k times! It takes too much time.
    # Instead, -k will be the new "starting index" (because
    # its right rotations), add query to that position,
    # and to mod n to wrap around.
    print nums[(-k + query) % n]
