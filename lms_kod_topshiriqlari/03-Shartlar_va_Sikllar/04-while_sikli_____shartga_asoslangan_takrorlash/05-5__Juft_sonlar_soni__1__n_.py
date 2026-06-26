# n beriladi.
# 1..n oralig‘ida nechta juft son borligini while bilan hisoblab chiqar.
n = int(input())
soni = 0
i = 1
while i <= n:
    if i % 2 == 0:
        soni += 1
    i += 1
print(soni)