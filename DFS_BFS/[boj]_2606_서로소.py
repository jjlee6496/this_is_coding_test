import sys

input = sys.stdin.readline

def find(parent, x):
    # 루트노드 찾기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
v = int(input())
e = int(input())

# 부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i


# 부모테이블 만들기
for i in range(e):
    a, b = map(int, input().split())
    union(parent, a, b)

result = -1 # 1 자기자신 빼기
for x in parent:
    if x == 1: # 1과 같은 집합이라면 감염되었다
        result += 1

print(result)