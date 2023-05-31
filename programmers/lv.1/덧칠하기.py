from collections import deque
def solutions(n, m, section):
    dq = deque(section)
    cnt = 1
    # 제일 왼쪽부터 m 만큼 칠해줌
    flag = section[0]+m-1
    while dq:
        if dq[0] <= flag:
            dq.popleft()
        else:
            cnt += 1
            flag = dq[0]+m-1
    return cnt