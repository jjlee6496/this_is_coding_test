import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 컴퓨터 갯수
m = int(input()) # 연결되어있는 컴퓨터 쌍

graph = [[] for _ in range(n+1)] # 그래프 초기화
visited = [0]*(n+1) # 방문 여부 초기화

# 그래프 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


dq = deque([1])

while dq:
    x = dq.popleft()
    if visited[x] == 0:
        visited[x] = 1
        for i in graph[x]:
            dq.append(i)
print(sum(visited)-1)