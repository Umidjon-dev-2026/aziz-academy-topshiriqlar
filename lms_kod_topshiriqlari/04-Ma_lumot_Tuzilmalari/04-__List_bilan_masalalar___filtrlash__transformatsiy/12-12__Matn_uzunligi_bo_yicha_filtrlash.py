# n va n ta so‘z beriladi.
# Uzunligi 3 dan katta bo‘lgan so‘zlarni list qilib chiqaring.
n = int(input())
matn = input().split()
list = []
for soz in matn:
    if len(soz) >= n:
        list.append(soz)
print(list)