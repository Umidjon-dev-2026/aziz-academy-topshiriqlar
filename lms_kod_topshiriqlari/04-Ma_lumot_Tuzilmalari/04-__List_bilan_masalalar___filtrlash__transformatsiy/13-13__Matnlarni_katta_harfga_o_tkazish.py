# n va n ta so‘z beriladi.
# Har bir so‘zni katta harflarga o‘tkazib list chiqaring.
n = int(input())
matn = input().split()
list = []
for son in matn:
    list.append(son.upper())
print(list)