import sys
import time
start = time.time()

input = sys.stdin.readline

N = int(input())
X, Y = 1, 1
data = input().split()

for i in data:
    if i == 'D':
        X += 1
    elif i == 'R':
        Y += 1
    elif i == 'U':
        if X == 1:
            continue
        else:
            X -= 1
    else:
        if Y == 1:
            continue
        else:
            Y -= 1
print(X, Y, sep=' ')
        


print("실행시간 :", time.time()-start,"초")