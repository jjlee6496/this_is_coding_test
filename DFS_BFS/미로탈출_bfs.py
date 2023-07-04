# import sys
# import time
# from collections import deque
# start = time.time()

# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [list(map(int, input().rstrip())) for _ in range(N)]

# # 이동할 네 가지 방향 정의
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# # BFS
# def bfs(x,y):
#     queue = deque()
#     queue.append((x, y))
#     # 큐가 빌 때 까지
#     while queue:
    
#         x, y = queue.popleft()
#         # 현재 위치에서 4가지 방향으로의 위치 확인
#         for i in range(4):
#             nx = x + dx[i]    
#             ny = y + dy[i]
#             # 미로찾기 공간을 벗어난 경우 무시
#             if nx<0 or nx>=N or ny<0 or ny>=M:
#                 continue
#             # 방문 위치가 갈수 없는 길일 경우 무시
#             if graph[nx][ny] == 0:
#                 continue
#             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#                 print(queue)
#     # 가장 오른쪾 아래까지의 최단 거리 반환
#     return graph[N-1][M-1]
# print(bfs(0,0))
# print("실행시간 :", time.time()-start,"초")

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]


# 갈수 있는 좌표(상하좌우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dq = deque()
dq.append((0, 0))
cnt = 0
while dq:

    a, b = dq.popleft()
    if (a, b) == (n, m):
        break
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:

            graph[nx][ny] = graph[a][b] + 1
            dq.append((nx, ny))

                
print(graph[n-1][m-1])