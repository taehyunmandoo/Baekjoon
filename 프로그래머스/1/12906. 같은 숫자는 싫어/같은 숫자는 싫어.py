def solution(arr):
    answer = [arr[0]]  # 첫 번째 요소를 먼저 추가

    for i in range(1, len(arr)):  # 두 번째 요소부터 비교
        if arr[i] != arr[i - 1]:  # 이전 요소와 다를 때만 추가
            answer.append(arr[i])

    return answer
