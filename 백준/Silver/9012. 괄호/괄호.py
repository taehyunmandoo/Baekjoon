import sys

input = sys.stdin.readline

T = int(input().strip())


for _ in range(T):
    data = input().strip()
    stack = []
    is_vps = True
    
    for char in data:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
            
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
        