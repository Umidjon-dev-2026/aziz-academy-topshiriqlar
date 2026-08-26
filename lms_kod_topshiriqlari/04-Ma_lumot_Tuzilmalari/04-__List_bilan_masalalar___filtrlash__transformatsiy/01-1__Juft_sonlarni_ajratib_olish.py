# n va n ta son beriladi.
# Faqat juft sonlardan iborat yangi list chiqaring.
n = int(input())
sonlar = map(int, input().split())
juft_sonlar = []
for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son)
print(juft_sonlar)