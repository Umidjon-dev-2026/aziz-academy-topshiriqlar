# n va n ta son beriladi.
# Faqat 10 dan katta sonlarni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
katta = []
for i in sonlar:
    if i > 10:
        katta.append(i)
        
print(katta)