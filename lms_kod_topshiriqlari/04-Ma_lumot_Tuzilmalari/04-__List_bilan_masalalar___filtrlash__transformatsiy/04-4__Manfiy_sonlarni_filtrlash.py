# n va n ta son beriladi.
# Faqat manfiy sonlarni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
manfiy = []
for i in sonlar:
    if i < 0:
        manfiy.append(i)
print(manfiy)