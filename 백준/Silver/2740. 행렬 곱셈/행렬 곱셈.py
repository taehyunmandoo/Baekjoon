N, M = map(int, input().split())

# 첫 번째 행렬 A 입력 받기
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
#print(A)
M, K = map(int, input().split())

# 두 번째 행렬 B 입력 받기
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

# 결과 행렬 C 초기화
C = [[0] * K for _ in range(N)]

# 행렬 곱셈 수행
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

# 결과 출력
for row in C:
    print(' '.join(map(str, row)))