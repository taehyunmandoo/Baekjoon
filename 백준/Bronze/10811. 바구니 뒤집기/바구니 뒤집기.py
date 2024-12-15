# 바구니의 수 N과 명령의 수 M을 입력받습니다.
N, M = map(int, input().split())

# 초기 바구니 상태를 설정합니다.
baskets = list(range(1, N + 1))

# M개의 명령을 순차적으로 수행합니다.
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]

# 최종 바구니 상태를 출력합니다.
print(' '.join(map(str, baskets)))
