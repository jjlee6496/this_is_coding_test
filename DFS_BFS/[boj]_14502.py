import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
temp_lab = [[0]*m for _ in range(n)] # 시뮬레이션 할때 복사용
max_safe_area = [0] # 함수 안에서 값을 바꾸기 위해 리스트로 선언

# bfs를 이용해 바이러스를 퍼트리는 함수
def spread_virus():
    dq = deque()
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 바이러스가 움직이는 방향(상하좌우)
    
    # temp_lab에 값 복사
    for i in range(n):
        for j in range(m):
            temp_lab[i][j] = lab[i][j]
            
            # 바이러스가 있는 좌표를 큐에 추가
            if temp_lab[i][j] == 2:
                dq.append((i, j))
    
    while dq:
        x, y = dq.popleft()
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            
            # 실험실 좌표 범위를 안넘어가고, 안전영역이면 바이러스가 퍼짐
            if 0<=nx<n and 0<=ny<m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                dq.append((nx, ny))
        


# 벽을 세우는 함수, 재귀적으로 모든 벽을 세우는 경우를 본다.
def build_wall(count):
    # 카운트가 3(모든 벽을 세운 경우)일 때 바이러스를 퍼트림
    if count == 3:
        spread_virus()
        # 바이러스를 퍼트린 후 안전영역 계산
        safe_area = sum(row.count(0) for row in temp_lab) # 리스트 컴프리헨션으로 0의 갯수를 세고 모두 더함
        max_safe_area[0] = max(max_safe_area[0], safe_area) # 가장 큰 안전영역을 담기 위함
        return
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1 # 벽 세우기
                build_wall(count+1) # 다음번 시뮬레이션 재귀로
                lab[i][j] = 0 # 한 가지가 끝나면 원상복구
build_wall(0)
print(max_safe_area[0])