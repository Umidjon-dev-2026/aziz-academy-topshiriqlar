# n va m beriladi.
# n qator bo‘lsin.
# Har qatorda 1 2 3 ... m chiqaring.
data = list(map(int, input().split()))
if len (data) == 1:
    print(0)
else:
    n, m = data
    if n == 0 or m == 0:
        print(0)
    else:
        for _ in range(n):
            print(*range(1, m + 1))