# 10개의 정수를 입력받아 리스트에 저장
numbers = []
for _ in range(10):
    num = int(input())
    numbers.append(num)

# 각 숫자를 42로 나눈 나머지를 리스트에 저장
remainders = []
for num in numbers:
    remainder = num % 42
    remainders.append(remainder)

# 리스트를 집합으로 변환하여 중복 제거
unique_remainders = set(remainders)

# 집합의 크기를 출력 (서로 다른 나머지의 개수)
print(len(unique_remainders))
