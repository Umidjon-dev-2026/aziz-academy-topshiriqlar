# Sonlar ketma-ket kiritiladi (har qatorda bitta).
# 0 kiritilganda to‘xtang.
# O‘rtacha qiymatni chiqaring.
# Agar 0 birinchi bo‘lsa, 0 chiqaring.
# Eslatma: o‘rtacha butun bo‘lsa ham float chiqishi mumkin.
y = 0
n = 0
while True:
    s = int(input())
    if s == 0:
        break
    y += s
    n += 1
if n == 0:
    print(0)
else:
    print(float(y / n))