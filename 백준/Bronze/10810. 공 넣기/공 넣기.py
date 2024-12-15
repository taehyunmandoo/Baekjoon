# 백준 10810번 - 공 넣기 (슬라이싱 활용)

# 입력 받기
N, M = map(int, input().split())

# 바구니 초기화
baskets = [0] * N

# M개의 명령 수행
for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = [k] * (j - i + 1)

# 결과 출력
print(' '.join(map(str, baskets)))
