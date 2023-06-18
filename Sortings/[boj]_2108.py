import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]
data = sorted(data)

# Mean
print(round(sum(data)/N))

# Median
if N % 2:
    print(data[N//2])
else:
    print((data[N//2]+data[N//2 + 1])/2)

# Mode
c = Counter(data)
common = c.most_common()

if len(common) == 1:
    print(common[0][0])
else:
    if common[0][1] == common[1][1]:
        print(common[1][0])
    else:
        print(common[0][0])

# Range
print(data[-1] - data[0])