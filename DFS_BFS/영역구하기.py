import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

# 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
cnt = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count = 1
            graph[i][j] = 1
            dq = deque()
            dq.append((i, j))
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        count += 1
                        dq.append((nx, ny))
            cnt.append(count)

for x in sorted(cnt):
    print(x, end=' ')