# n va n ta son beriladi.
# Bo‘sh list yarating.
# Har bir sonni listning boshiga insert(0, x) qilib qo‘shing.
# Natijada list teskari bo‘lib chiqadi.
# Listni chiqaring.
n = int(input())
x = input().split()
sonlar = []
for b in x:
    sonlar.insert(0, int(b))
print(sonlar)