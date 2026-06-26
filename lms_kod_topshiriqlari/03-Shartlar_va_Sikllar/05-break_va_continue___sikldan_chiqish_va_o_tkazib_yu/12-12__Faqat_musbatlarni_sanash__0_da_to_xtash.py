# Sonlar ketma-ket kiritiladi.
# 0 kiritilganda break.
# Manfiy bo‘lsa continue.
# Faqat musbat sonlar sonini hisoblab chiqaring.
count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n < 0:
        continue
    count += 1
print(count)