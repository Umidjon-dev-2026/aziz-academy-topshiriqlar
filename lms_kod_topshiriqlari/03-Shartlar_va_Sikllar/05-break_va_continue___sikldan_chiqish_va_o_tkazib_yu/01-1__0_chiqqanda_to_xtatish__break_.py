# Sonlar ketma-ket kiritiladi (har qatorda bitta).
# 0 kiritilganda break qiling.
# 0 gacha bo‘lgan sonlar yig‘indisini chiqaring (0 hisobga olinmaydi).
s = 0
while True:
    a = int(input())
    if a == 0:
        break
    s += a 
print(s)