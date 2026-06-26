# Sonlar ketma-ket kiritiladi.
# Birinchi toq son kelishi bilan break.
# Toq son kelguncha kiritilgan sonlar yig‘indisini chiqar.
# (Agar birinchi son toq bo‘lsa, 0 chiqishi kerak.)
s = 0
while True:
    n = int(input())
    if n % 2 != 0:
        break
    s += n 
print(s)