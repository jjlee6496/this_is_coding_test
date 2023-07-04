import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1,0,0,1]
dy = [0,1,-1,0]
result = []

def dfs(x,y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx > m or ny < 0 or ny >=m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)