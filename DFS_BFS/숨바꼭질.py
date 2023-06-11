import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [0]*100001

dq = deque()
dq.append(n)
while dq:
    x = dq.popleft()
    if x == k:
        print(graph[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0<=nx<len(graph) and graph[nx]==0:
            graph[nx] = graph[x] + 1
            dq.append(nx)
            
    