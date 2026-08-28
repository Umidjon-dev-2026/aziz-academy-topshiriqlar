# n va n ta son beriladi.
# 0 < x < 100 bo‘lgan sonlarni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
list = []
for son in sonlar:
    if 0 < son < 100:
        list.append(son)
print(list)