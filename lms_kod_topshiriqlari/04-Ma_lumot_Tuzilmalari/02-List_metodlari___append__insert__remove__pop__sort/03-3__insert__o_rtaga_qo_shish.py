# n = int(input())
# lst = list(map(int, input().split()))
# val = int(input())
# 1-indexga val ni insert qiling va listni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
val = int(input())
sonlar.insert(1, val)
print(sonlar)