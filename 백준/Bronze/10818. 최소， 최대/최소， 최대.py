# 입력 받기
N = int(input())
data = list(map(int, input().split()))

# 최솟값과 최댓값 초기화
min_val = data[0]
max_val = data[0]

# 리스트를 순회하며 최솟값과 최댓값 찾기
for num in data:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

# 결과 출력
print(min_val, max_val)
