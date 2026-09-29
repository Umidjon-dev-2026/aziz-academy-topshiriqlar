# INPUT: 1 qatorda butun sonlar
# VAZIFA: faqat 10 dan katta sonlarni qoldiring
# OUTPUT: sonlar space bilan
# Agar bo‘sh bo‘lsa: BO'SH
a = list(map(int, input().split()))
katta = [str(x) for x in a if x > 10]
if katta:
    print(" ".join(katta))
else:
    print("BO'SH")