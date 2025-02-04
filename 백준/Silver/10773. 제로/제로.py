import sys

input = sys.stdin.readline

K = int(input().strip())

stack = []

for _ in range(K):
    data = int(input().strip())
    if data == 0:
        if stack:
            stack.pop()
    else:
        stack.append(data)
print(sum(stack))
