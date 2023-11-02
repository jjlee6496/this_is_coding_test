import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int,  input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]

# 그래프 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

def dfs(x, y , graph):
    cnt = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    def recursive_dfs(a, b):
        nonlocal cnt
        if 0 <= a < m and 0 <= b < n and graph[a][b] == 0:
            graph[a][b] = 1
            cnt += 1
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                recursive_dfs(nx, ny)
    if graph[x][y] == 0:
        recursive_dfs(x, y)
        
    return cnt

answer = []
for i in range(m):
    for j in range(n):
        ans = dfs(i, j, graph)
        if ans:
            answer.append(ans)
print(len(answer))
for i in sorted(answer):
    print(i, end=' ')