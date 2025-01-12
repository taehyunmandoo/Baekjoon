def solution(s):
    count = 0
    for char in s:  # s의 각 문자를 char로 순회
        if char == "p" or char == "P":  # 'p' 또는 'P'라면
            count += 1
        elif char == "y" or char == "Y":  # 'y' 또는 'Y'라면
            count -= 1

    if count == 0:
        return True
    else:
        return False
