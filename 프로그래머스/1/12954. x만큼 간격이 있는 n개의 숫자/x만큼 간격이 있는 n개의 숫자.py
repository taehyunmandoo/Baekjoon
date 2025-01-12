def solution(x, n):
    answer = [] # 빈 리스트 선언 
    for i in range(1, n+1): # i = 1부터 n까지 반복 실행 (n번)
        answer.append(x*i) # answer 마지막에 x*i 를 삽입
    return answer # 반복문 종료 후 결과 값 반환
        