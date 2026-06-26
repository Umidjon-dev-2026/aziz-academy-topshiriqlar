# n beriladi.
# 1..n ichida 9 ga karrali sonlarni continue bilan tashlab ket.
# Qolgan sonlar yig‘indisini chiqar.
n = int(input())
s = 0 
for i in range(1, n + 1):
    if i % 9 == 0:
        continue
    s += i 
print(s)
        