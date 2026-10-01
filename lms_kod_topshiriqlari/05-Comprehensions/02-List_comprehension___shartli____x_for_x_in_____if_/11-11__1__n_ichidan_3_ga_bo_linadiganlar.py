# INPUT: n
# VAZIFA: 1 dan n gacha bo‘lgan sonlardan faqat 3 ga bo‘linadiganlarini chiqaring
# OUTPUT: sonlar space bilan
# Agar bo‘sh bo‘lsa: BO'SH
n = int(input())
natija = [str(i) for i in range(1, n + 1) if i % 3 == 0]

if natija:
    print(*(natija))
else:
    print("BO'SH")