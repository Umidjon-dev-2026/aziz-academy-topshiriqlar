# Sonlar ketma-ket kiritiladi.
# 0 kiritilganda break.
# Manfiy sonlar bo‘lsa continue (yig‘indiga qo‘shmang).
# Natijada faqat musbat sonlar yig‘indisini chiqaring.
yigindi = 0
while True:
    son = int(input())
    if son == 0:
        break
    if son < 0:
        continue
    yigindi += son
print(yigindi)