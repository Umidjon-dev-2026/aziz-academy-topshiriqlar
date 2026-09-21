# Kodingizni shu yerga yozing
n = int(input())
numbers = set()
for _ in range(n):
    numbers.add(int(input()))
target = int(input())
print(target in numbers)