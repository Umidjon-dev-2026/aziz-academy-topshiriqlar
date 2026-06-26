# n beriladi.
# 1..n oralig‘idagi faqat toq sonlarni chiqar.
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)