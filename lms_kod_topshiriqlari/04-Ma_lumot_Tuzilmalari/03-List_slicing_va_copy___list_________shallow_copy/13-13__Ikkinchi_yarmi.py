# n va n ta son beriladi.
# Listning ikkinchi yarmini slicing bilan chiqaring.
# (Agar toq bo‘lsa, o‘rtadagi kirmasin)
n = int(input())
x = list(map(int, input().split()))
print(x[(n + 1) // 2:])