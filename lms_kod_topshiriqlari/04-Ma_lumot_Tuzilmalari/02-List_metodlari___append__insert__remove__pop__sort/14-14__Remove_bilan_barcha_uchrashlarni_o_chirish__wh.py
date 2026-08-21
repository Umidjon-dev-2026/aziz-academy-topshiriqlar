# n va n ta son beriladi, keyin x beriladi.
# Listdan x qiymatli barcha elementlarni o‘chiring.
# (Eslatma: while x in lst: lst.remove(x))
# Oxirida listni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
x = int(input())
while x in sonlar:
    sonlar.remove(x)
print(sonlar)