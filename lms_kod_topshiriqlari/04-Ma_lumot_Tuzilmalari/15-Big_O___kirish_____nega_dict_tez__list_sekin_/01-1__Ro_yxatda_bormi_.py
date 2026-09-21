# Kodingizni shu yerga yozing
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
target = int(input())
if target in numbers:
    print("bor")
else:
    print("yo'q")