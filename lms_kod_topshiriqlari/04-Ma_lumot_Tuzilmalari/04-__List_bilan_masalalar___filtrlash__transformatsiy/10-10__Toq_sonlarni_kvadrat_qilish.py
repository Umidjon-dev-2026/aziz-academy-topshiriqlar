# n va n ta son beriladi.
# Faqat toq sonlarni olib, kvadratidan iborat list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
list = []
for son in sonlar:
    if son % 2 != 0:
        list.append(son * son)
print(list)