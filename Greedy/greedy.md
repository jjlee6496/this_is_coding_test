# 그리디 알고리즘이란?

---

그리디 알고리즘은 단순하지만 강력한 문제 해결 방법이다. 이름 그대로 어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘이다. 여기서 탐욕적이라는 말은 ‘현재 상황에서 지금 당장 좋은 것만 고르는 방법’을 의미한다. 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다.

## 예제1

[거스름돈](https://www.notion.so/2e1b5fece8054b4898c8b3a8862d4eb1) 

# 그리디 알고리즘의 정당성

---

그리디 알고리즘을 모든 알고리즘 문제에 적용할 수는 없다. → 먼저 그 해법이 정당한지 검토해야 한다. 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다. 

대부분의 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다.

## 예제 2 큰수의 법칙

---

### 문제

동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수로 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

- 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만든다
- 예를 들어 2,4,5,4,6 으로 이루어진 배열이 있을 때 특정한 인덱스의 수가 연속해서 세 번 까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6+6+5+6+6+5인 46이 된다.
- 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어, 3,4,3,4,3 으로 이루어진 배열이 있을 때 M=7, K=2일 때 4+4+4+4+4+4+4=28이 가능

### 입력

- 첫째 줄에 N(2≤N≤1,000), M(1≤M≤10,000), K(1≤K≤10,000) 의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

### 출력

- 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

```
입력 예시
5 8 3
2 4 5 4 6

출력 예시
46

```

## 풀이

```python
import sys
# 입력
input = sys.stdin.readline
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

# 풀이
data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K):
        if M==0:
            break
        result += first
        M -= 1
    if M==0:
        break
    result += second
    M -= 1
print(result)
```

## 풀이2

이러한 문제는 수열로도 풀이가 가능하다. 반복되는 수열에 대해서 파악해보면,

반복되는 수열의 길이는 K+1이 된다. 

예시 1로 설명해 보자면 K=3 으로 6,6,6,5가 반복이 된다. 따라서 K+1만큼 수열이 반복.

따라서 M=8을 4로 나눈 횟수 2만큼 반복되게 된다. 한편 M이 K+1로 나누어 떨어지지 않는 횟수까지 고려하여 큰 수가 더해지는 횟수를 구한다.

```python
count = M//(K+1)*K + M%(K+1) # ->큰 수가 등장하는 횟수

result = count*first + (M-count)*second
```

## 예제 3: 숫자 카드 게임

---

### 문제

숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는게임이다. 다음은 규칙

1. 카드가 N$\times$M 형태로 놓여있다. N=행, M=열
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.

### 입력

- 첫째 줄에 카드들이 놓은 행, 열 N, M이 공백을 기준으로 자연수로 주어짐.(1≤N, M≤100)
- 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수.

### 출력

- 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

```
입력 예시
3 3
3 1 2
4 1 4 
2 2 2

출력 예시
2

입력 예시
2 4
7 3 1 8
3 3 3 4

출력 예시
3
```

### 풀이

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [min(map(int, input().split())) for _ in range(N)]
print(max(a))
```

## 예제 4: 1이 될 때 까지

---

### 문제

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 다, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

### 입력

- 첫째 줄에 N(2≤N≤100,000)과 K가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

### 출력

- 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 구한다

```
입력 예시
25 5

출력 예시
2
```

### 풀이

```python
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
i = 0
while True:
    if N==1: break
    if N%K == 0:
        N /= K
        i += 1
    else:
        N -= 1
        i += 1
print(i)
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3d3b935-4486-4cd5-95f0-662dcdf5b8ec/Untitled.png)

위 코드도 맞지만 단위가 클때 1씩 계속 빼는 것은 낭비이다.

따라서 K의 배수가 되는만큼 빼기

ex) 27 4 라하면 27-24 = 3만큼 횟수를 더해주고 나누기횟수 +1

27 → 24 → 6 → 4 → 1

+3 +1 +2 +1

또한  중간에 남은 수 N이 K보다 작을때에는 반복문 탈출 → N-1만큼 더해줌

### 풀이2

 

```
import sys
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
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a123ac42-99d0-4fa0-b7ac-fff6d0b754c3/Untitled.png)