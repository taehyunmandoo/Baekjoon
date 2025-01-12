def solution(n):
    list = []
    for i in range(1,n+1):
        if n%i == 1:
            list.append(i)
    answer = min(list)
    return answer
