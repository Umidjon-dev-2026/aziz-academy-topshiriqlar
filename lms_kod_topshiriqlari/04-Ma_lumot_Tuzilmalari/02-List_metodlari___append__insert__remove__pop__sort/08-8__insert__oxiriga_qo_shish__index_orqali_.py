# n = int(input())
# lst = list(map(int, input().split()))
# val = int(input())
# insert(len(lst), val) bilan oxiriga qo'shing va listni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
val = int(input())
sonlar.insert(len(sonlar), val)
print(sonlar)