# 입력 처리
A, B, C = map(int, input().split())

# 조건에 따라 상금 계산
if A == B == C:  # 같은 눈 3개
    prize = 10000 + A * 1000
elif A == B or A == C:  # 같은 눈 2개 (A와 B 또는 A와 C)
    prize = 1000 + A * 100
elif B == C:  # 같은 눈 2개 (B와 C)
    prize = 1000 + B * 100
else:  # 모두 다른 경우
    prize = max(A, B, C) * 100

# 결과 출력
print(prize)
