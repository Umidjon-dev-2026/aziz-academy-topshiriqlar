# n beriladi.
# for bilan 1..n ichida 7 ga karrali sonlarni chiqar.
# Agar yo‘q bo‘lsa, hech narsa chiqmasin.
n = int(input())
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i)