# n va n ta son beriladi.
# for bilan eng katta sonni topib chiqar.
# (max ishlatmaymiz)
n = int(input())
sonlar = list(map(int, input().split()))
eng_katta = sonlar[0]
for son in sonlar:
    if son > eng_katta:
        eng_katta = son
print(eng_katta)