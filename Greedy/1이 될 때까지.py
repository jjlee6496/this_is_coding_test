import sys
import time
start = time.time()

input = sys.stdin.readline

N, K = map(int, input().split())
i = 0
while True:
    target = (N//K) * K
    i += (N - target)
    N = target
    
    # 중간에 N보다 K가 작아지거나 N이 1이되었을 경우 탈출
    if N < K: break
    
    # K로 N 나눠주기
    i += 1
    N //= K
# 마지막으로 1이 될때까지 더해주기    
i += N-1
print(i)
print("실행시간 :", time.time()-start,"초")