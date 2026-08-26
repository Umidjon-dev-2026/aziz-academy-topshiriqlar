# n va n ta son beriladi.
# Faqat toq sonlardan iborat list chiqaring.
n = int(input())
sonlar = map(int, input().split())
toq_sonlar = []
for son in sonlar:
    if son % 2 != 0:
        toq_sonlar.append(son)
print(toq_sonlar)