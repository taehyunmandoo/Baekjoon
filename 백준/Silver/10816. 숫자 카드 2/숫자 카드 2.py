N = int(input()) 
N_list = list(map(int, input().split()))
M = int(input()) 
M_list = list(map(int, input().split()))

N_list.sort()

# 이진탐색으로 첫 번째 등장 위치를 찾는 함수
def first_occurrence(search, start, end):
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] >= search:
            end = mid - 1
        else:
            start = mid + 1
    return start

# 이진탐색으로 마지막 등장 위치를 찾는 함수
def last_occurrence(search, start, end):
    while start <= end:
        mid = (start + end) // 2
        if N_list[mid] > search:
            end = mid - 1
        else:
            start = mid + 1
    return end

for value in M_list:
    # 첫 등장 위치와 마지막 등장 위치를 각각 구함
    first = first_occurrence(value, 0, N - 1)
    last = last_occurrence(value, 0, N - 1)
    
    # 개수를 계산해서 출력
    if first <= last:
        print(last - first + 1, end=' ')
    else:
        print(0, end=' ')