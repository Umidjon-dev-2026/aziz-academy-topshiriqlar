# n va n ta son beriladi.
# Faqat musbat sonlarni chiqaring.
n = int(input())
sonlar = map(int, input().split())
musbat_sonlar = []
for son in sonlar:
    if son > 0:
        musbat_sonlar.append(son)
print(musbat_sonlar)        