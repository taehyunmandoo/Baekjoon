def sort_partial(arr, n, k):
    size = n // k  # 부분 배열의 크기
    result = []
    
    for i in range(0, n, size):
        part = arr[i:i + size]
        part.sort()  # 부분 배열을 정렬
        result.extend(part)  # 정렬된 부분 배열을 결과에 추가
    
    return result

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# 부분 배열을 정렬하고 결과를 출력
result = sort_partial(arr, n, k)
print(' '.join(map(str, result)))
