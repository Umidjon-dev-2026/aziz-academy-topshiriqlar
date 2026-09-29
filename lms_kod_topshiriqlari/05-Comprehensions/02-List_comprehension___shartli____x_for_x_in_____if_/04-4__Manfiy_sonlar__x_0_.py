# INPUT: 1 qatorda butun sonlar
# VAZIFA: faqat 0 dan kichik sonlarni qoldiring
# OUTPUT: manfiylar space bilan
# Agar bo‘sh bo‘lsa: BO'SH
a = list(map(int, input().split()))
negative = [str(x) for x in a if x < 0]
if negative:
    print(" ".join(negative))
else:
    print("BO'SH")