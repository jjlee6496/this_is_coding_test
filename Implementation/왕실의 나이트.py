import sys
import time
start = time.time()

input = sys.stdin.readline

a = input()
X = ord(list(a)[0]) - ord('a') + 1
Y = int(list(a)[1])
move = [(-2,-1),(-2,1),(-1,2),(-1,2),(1,-2),(1,2),(2,1),(2,-1)]
result = 0

for x, y in move:
   if (X+x>0 and X+x<9) and (Y+y>0 and Y+y<9):
        result += 1

print(result)

print("실행시간 :", time.time()-start,"초")