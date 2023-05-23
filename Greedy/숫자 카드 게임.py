import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [min(map(int, input().split())) for _ in range(N)]
print(max(a))