# n beriladi.
# 1..n bo‘yicha qo‘shish jadvali chiqaring: i+j.
# Jadval o‘lchami n x n.
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n:
            print(i + j, end="")
        else:
            print(i + j, end=" ")
    print()