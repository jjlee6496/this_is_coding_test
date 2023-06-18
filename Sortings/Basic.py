import sys
import time
input = sys.stdin.readline

N = int(input())
data = [int(input()) for _ in range(N)]


# 선택정렬
def select_sort(data):
    for i in range(len(data)):
        min_index = i # 첫번째 원소를 min으로 잡고
        for j in range(i+1, len(data)):
            # 두번째부터 반복: 만약 min 보다 작은 데이터가 나오면
            if data[min_index] > data[j]:
                # min을 바꿔주고
                min_index = j
        # 원래 min과 바뀐 min을 바꿔준다
        data[i], data[min_index] = data[min_index], data[i]
    
    return data

# 삽입 정렬
def insert_sort(data):
    for i in range(1, len(data)): # 두번째 원소부터
        for j in range(i, 0, -1): # 첫번재 원소까지 거꾸로
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    return data


# 퀵 정렬 - General 한 버전
# def quick_sort(data, start, end):
#     if len(data) <= 1:
#         return data
    
#     pivot = start # 첫번째 원소는 피벗
#     left = start + 1 # 두번째 원소 = 왼쪽 포인트
#     right = end # 마지막 원소 = 오른쪽 포인트
    
#     while (left <= right):
        
#         # 왼쪽포인트가 end와 같거나 왼쪽에 있고 오른쪽포인트가 피벗보다 오른쪽에 있으면
#         while(left <= end and data[left] <= data[pivot]):
#             left += 1
        
#         # 오른쪽 포인트가 start보다 크고 피벗보다 클 때
#         while(right > start and data[right] > data[pivot]):
#             right -= 1
        
#         # 엇갈렸다면 pivot과 오른쪽 포인트를 스왑
#         if(left > right):
#             data[right], data[pivot] = data[pivot], data[right]

#         # 엇갈리지 않았다면 pivot과 왼쪽 포인트를 스왑        
#         else:
#             data[left], data[pivot] = data[pivot], data[left]
            
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각자 정렬 수행
#     quick_sort(data, start, right-1)
#     quick_sort(data, right+1, end)
    
#     return data

# 퀵 정렬 - Pythonic 한 버전, 백준서 메모리 초과
def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    tail = data[1:]
    
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)
# 출력
start = time.time()
# data = select_sort(data)
# data = insert_sort(data)
data = quick_sort(data)

for i in data:
    print(i)

print('실행시간: ', time.time() - start)