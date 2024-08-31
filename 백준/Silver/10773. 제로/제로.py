k = int(input())

Stack = list()

for i in range(k):
    num = int(input())
    if num == 0:
        Stack.pop()
        continue
        
    Stack.append(num)

print(sum(Stack))