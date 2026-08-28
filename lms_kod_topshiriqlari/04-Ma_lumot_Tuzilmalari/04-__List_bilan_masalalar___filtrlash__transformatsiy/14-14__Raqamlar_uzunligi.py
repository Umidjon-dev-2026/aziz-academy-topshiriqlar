# n va n ta son beriladi.
# Har bir son nechta raqamdan iboratligini list qilib chiqaring.
n = int(input())
sonlar = input().split()
uzunlik = []
for son in sonlar:
    uzunlik.append(len(son))
print(uzunlik)