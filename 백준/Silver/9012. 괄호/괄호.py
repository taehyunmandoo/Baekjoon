t = int(input())

for i in range(t):
    stack = list(input())
    sum = 0

    for j in range(len(stack)):
        if stack[j] == "(":
            sum += 1
        else:
            sum -= 1

        if sum < 0: # ())일 때
            print("NO")
            break

    if sum > 0:     # 짝 개수가 맞지 않을 떄
        print("NO")
    elif sum == 0:  # 짝 개수가 똑같을 때
        print("YES")