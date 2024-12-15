# 입력 받기
N = 9
data_list = []
for _ in range(N):
    data = int(input())
    data_list.append(data)

# 최댓값 찾기
max_value = max(data_list)

# 최댓값의 위치 찾기 (1부터 시작)
position = data_list.index(max_value) + 1

# 결과 출력
print(max_value)
print(position)
