import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())

# 배열 초기화
graph = [[0]*n for _ in range(m)] # n,m 주의

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


def bfs(graph, x, y):
    # 움직일 수 있는 좌표 (상하좌우)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    cnt = 0
    if graph[x][y] == 0:
        dq = deque()
        dq.append((x, y))
        graph[x][y] = 1
        cnt += 1
        while dq:
            a, b = dq.popleft()
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
                    graph[nx][ny] = 1
                    cnt += 1
                    dq.append((nx, ny))
   
    return cnt

answer = []
for i in range(m):
    for j in range(n):
        ans = bfs(graph, i, j)
        if ans:
            answer.append(ans)
print(len(answer))
for x in sorted(answer):
    print(x, end=' ')