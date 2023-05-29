import sys
import time
start = time.time()

input = sys.stdin.readline

N, M = map(int, input().split())

# 입력
graph = [list(map(int, input().rstrip())) for _ in range(N)]
#DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if graph[x][y] == 0:
        print(graph)
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        print('done')
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
print("실행시간 :", time.time()-start,"초")