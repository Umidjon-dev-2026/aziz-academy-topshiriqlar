# n beriladi.
# 1..n oralig‘ida 3 ga karrali sonlarni chiqarma (continue).
# Qolgan sonlarni har qatorda bitta chiqar.
n = int(input())
i = 1
while i <= n:
    if i % 3 == 0:
        i += 1 
        continue
    print(i)
    i += 1