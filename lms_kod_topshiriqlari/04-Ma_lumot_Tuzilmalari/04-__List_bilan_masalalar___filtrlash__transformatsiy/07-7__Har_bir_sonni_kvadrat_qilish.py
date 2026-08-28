# n va n ta son beriladi.
# Har bir sonning kvadratidan iborat list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
kvadrat = []
for son in sonlar:
    kvadrat.append(son * son)
print(kvadrat)