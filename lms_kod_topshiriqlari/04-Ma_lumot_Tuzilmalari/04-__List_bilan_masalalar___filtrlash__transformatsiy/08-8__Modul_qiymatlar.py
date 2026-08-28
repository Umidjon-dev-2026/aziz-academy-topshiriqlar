# n va n ta son beriladi.
# Har bir sonning modulidan iborat list chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
qiymat = []
for son in sonlar:
    qiymat.append(abs(son))
print(qiymat)