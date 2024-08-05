n, k = map(int, input().split())

coin_types = []
count = 0

#입력 받는 부분
for _ in range(n):
    i = int(input())
    coin_types.append(i)
        
coin_types.sort(reverse=True)

for coin in coin_types:
    if k // coin > 0:
        count = count + k // coin
        k = k % coin
    else: 
        continue
    
print(count)