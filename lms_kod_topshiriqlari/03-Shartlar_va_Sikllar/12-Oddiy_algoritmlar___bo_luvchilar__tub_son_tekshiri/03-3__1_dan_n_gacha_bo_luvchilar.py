# n beriladi.
# 1 dan n gacha bo‘lgan bo‘luvchilarni chiqaring.
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        print(i)