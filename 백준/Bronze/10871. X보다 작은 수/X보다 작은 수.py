# 입력 처리
N, X = map(int, input().split())
data = list(map(int, input().split()))

# 결과 리스트에 X보다 작은 값 추가
result = [i for i in data if i < X]

# 결과 출력
print(" ".join(map(str, result)))
