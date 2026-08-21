# n = int(input())
# lst = list(map(int, input().split()))
# Birinchi elementni pop(0) qiling va chiqar.
# Keyin listni chiqar.
x = int(input())
sonlar = list(map(int, input().split()))
first = sonlar.pop(0)
print(first)
print(sonlar)