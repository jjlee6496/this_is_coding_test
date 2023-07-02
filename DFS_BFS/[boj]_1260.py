import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):  
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    if visited[v] == 0:
        visited[v] = 1
        print(v, end=' ')
        for x in sorted(graph[v]):
            dfs(x)


def bfs(v):
    visited = [0]*(n+1)
    dq = deque()
    dq.append(v)
    while dq:
        x = dq.popleft()
        if visited[x] == 0:
            visited[x] = 1
            print(x, end=' ')
            for i in sorted(graph[x]):
                dq.append(i)
dfs(v)
print()
bfs(v)