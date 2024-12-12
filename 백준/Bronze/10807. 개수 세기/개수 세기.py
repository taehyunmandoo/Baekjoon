N = int(input())

data = list(map(int, input().split()))
    
v = int(input())

cnt = 0 
for i in data:
	if i == v:
		cnt += 1
print(cnt)
    