import sys
import time
start = time.time()

input = sys.stdin.readline

N = int(input())
result = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                result += 1
                
print(result)


print("실행시간 :", time.time()-start,"초")