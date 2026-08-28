# n va n ta son beriladi.
# Har bir sonni 2 ga ko‘paytirib yangi list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
lis = []
for n in sonlar:
    lis.append(n * 2)
print(lis)