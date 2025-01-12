def solution(n):
    a = []  # 결과 리스트
    s = reversed(str(n))  # 문자열로 변환 후 뒤집음
    for i in s:  # 각 문자를 순회
        a.append(int(i))  # 정수로 변환 후 추가
    return a
