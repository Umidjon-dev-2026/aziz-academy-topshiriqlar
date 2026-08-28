# n va n ta son beriladi.
# Faqat juft sonlarni olib, ularni 10 ga ko‘paytirib list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
list = []
for son in sonlar:
    if son % 2 == 0:
        list.append(son * 10)
print(list)