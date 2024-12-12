# 입력받기
H, M = map(int, input().split())

# 45분 전 시간 계산
if M >= 45:
    M -= 45
else:
    M = M + 60 - 45  # 분을 이전 시간으로 보정
    H = H - 1        # 한 시간 줄이기
    if H < 0:        # 시간이 음수가 되면 23으로 설정
        H = 23

# 결과 출력
print(H, M)
