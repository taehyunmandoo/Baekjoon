# 1. 시험 과목의 개수 N을 입력받습니다.
N = int(input())

# 2. N개의 점수를 리스트로 입력받습니다.
scores = list(map(int, input().split()))

# 3. 최고 점수 M을 찾습니다.
max_score = max(scores)

# 4. 점수 변환
# 최고 점수가 0인 경우를 대비하여 조건문을 추가합니다.
if max_score == 0:
    normalized_scores = [0 for _ in scores]
else:
    normalized_scores = [(score / max_score) * 100 for score in scores]

# 5. 평균 계산
average = sum(normalized_scores) / N

# 6. 결과 출력 (소수점 이하 6자리)
print(f"{average:.6f}")
