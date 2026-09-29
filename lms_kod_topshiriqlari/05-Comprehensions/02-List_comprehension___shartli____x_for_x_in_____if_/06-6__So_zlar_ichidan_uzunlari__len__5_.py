# INPUT: 1 qatorda so‘zlar (space bilan)
# VAZIFA: uzunligi 5 yoki undan katta so‘zlarni qoldiring
# OUTPUT: so‘zlar space bilan
# Agar bo‘sh bo‘lsa: BO'SH
a = input().split()
katta = [x for x in a if len(x) >= 5]
if katta:
    print(" ".join(katta))
else:
    print("BO'SH")