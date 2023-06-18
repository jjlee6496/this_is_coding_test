import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

answer = []
result = 0
for x in sorted(data):
    result += x
    answer.append(result)

print(sum(answer))