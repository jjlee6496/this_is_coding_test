import sys
# 입력
input = sys.stdin.readline
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

# 풀이
data.sort()
first = data[N-1]
second = data[N-2]

count = M//(K+1)*K + M%(K+1)
print(count*first + (M-count)*second)