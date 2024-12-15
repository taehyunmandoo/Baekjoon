# 백준 10813번 - 공 바꾸기

# 1. 입력 받기
N, M = map(int, input().split())

# 2. 바구니 초기화
# 각 바구니에는 처음에 해당 번호의 공이 들어있습니다.
baskets = list(range(1, N + 1))

# 3. M개의 명령 수행
for _ in range(M):
    i, j = map(int, input().split())
    # 바구니 번호는 1부터 시작하므로, 인덱스는 0부터 시작합니다.
    # 따라서, i번 바구니는 인덱스 i-1, j번 바구니는 인덱스 j-1입니다.
    # 공을 서로 교환합니다.
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

# 4. 결과 출력
print(' '.join(map(str, baskets)))
