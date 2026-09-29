# INPUT: 1 qatorda butun sonlar
# VAZIFA: faqat 0 dan katta sonlarni qoldiring
# OUTPUT: musbatlar space bilan
# Agar bo‘sh bo‘lsa: BO'SH
a = list(map(int, input().split()))
positive = [str(x) for x in a if x > 0]
if positive:
    print(" ".join(positive))
else:
    print("BO'SH")