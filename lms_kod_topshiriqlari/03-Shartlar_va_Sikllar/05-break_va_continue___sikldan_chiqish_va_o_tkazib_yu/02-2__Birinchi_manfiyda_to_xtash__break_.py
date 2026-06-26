# Sonlar ketma-ket kiritiladi.
# Birinchi manfiy son kelishi bilan break qiling.
# Manfiygacha kiritilgan musbat/0 sonlar sonini chiqaring.
s = 0 
while True:
    son = int(input())
    if son < 0:
        break
    s += 1 
print(s)