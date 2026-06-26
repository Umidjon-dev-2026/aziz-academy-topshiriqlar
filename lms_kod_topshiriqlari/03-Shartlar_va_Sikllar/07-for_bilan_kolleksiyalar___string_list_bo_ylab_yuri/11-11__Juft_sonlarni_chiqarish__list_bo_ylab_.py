# n va n ta son beriladi.
# for bilan faqat juft sonlarni har qatorda bitta chiqar.
# Agar juft bo‘lmasa, hech narsa chiqmasin.
n = int(input())
a = list(map(int, input().split()))
for x in a:
    if x % 2 == 0:
        print(x)