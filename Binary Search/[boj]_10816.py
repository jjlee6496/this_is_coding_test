import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
data = list(map(int, input().split()))

def count(arr, left, right):
    r = bisect_right(arr, right)
    l = bisect_left(arr, left)
    return r - l


for i in data:
    print(count(nums, i, i), end=' ')