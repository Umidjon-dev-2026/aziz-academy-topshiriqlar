# n = int(input())
# lst = list(map(int, input().split()))
# Oxirgi elementni pop qiling va chiqar.
# Keyin qolgan listni ham chiqar.
n = int(input())
sonlar = list(map(int, input().split()))
oxirgi = sonlar.pop()
print(oxirgi)
print(sonlar)