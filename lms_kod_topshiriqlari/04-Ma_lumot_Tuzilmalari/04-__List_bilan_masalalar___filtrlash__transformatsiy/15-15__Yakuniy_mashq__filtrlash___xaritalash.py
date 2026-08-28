# n va n ta son beriladi.
# Faqat musbat sonlarni oling.
# Ularni 2 ga ko‘paytiring.
# Natijaviy listni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
list = []
for son in sonlar:
    if son > 0:
        list.append(son * 2)
print(list)