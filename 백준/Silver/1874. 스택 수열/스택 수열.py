n = int(input())

count = 1
stack = []
result = []

for i in range(1, n + 1): #데이터 개수만큼 반복
  data = int(input())
  while count <= data:
      stack.append(count)
      count += 1
      result.append('+')
  if stack[-1] == data:
      stack.pop()
      result.append('-')
  else:
      print('NO')
      exit(0)

print('\n'.join(result))