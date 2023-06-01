import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)] # graph 초기화
visited = [0]*(n+1) #방문여부

for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b] # graph[a].append(b)
    graph[b] += [a] # graph[b].append(a)

# result1 = []
# result2 = []

def dfs(i):
    visited[i] = 1
    # result1.append(i)
    print(i, end=' ')
    for x in sorted(graph[i]):
        if visited[x]==0:
            dfs(x)
dfs(v)
visited = [0]*(n+1) #방문여부
visited[v] = 1
q = deque([v])
def bfs(i):
    while q:
        a = q.popleft()
        # result2.append(a)
        print(a, end=' ')
        for x in sorted(graph[a]):
            if visited[x] == 0:
                q.append(x)
                visited[x] = 1
print()
bfs(v)
# print(result1)
# print(result2)
    
    