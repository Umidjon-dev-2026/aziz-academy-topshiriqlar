# n = int(input())
# lst = list(map(int, input().split()))
# val = int(input())
# Boshiga val ni insert qiling va listni chiqaring.
a = int(input())
sonlar = list(map(int, input().split()))
val = int(input())
sonlar.insert(0, val)
print(sonlar)