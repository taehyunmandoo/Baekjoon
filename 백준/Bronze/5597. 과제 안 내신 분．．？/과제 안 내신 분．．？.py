N = 28
data = list()

# 28명의 제출한 학생 번호를 입력받아 집합에 저장
for _ in range(N):
    num = int(input())
    data.append(num)

# 1부터 30까지의 번호 중 제출하지 않은 번호를 찾아 출력
for i in range(1, 31):
    if i not in data:
        print(i)
