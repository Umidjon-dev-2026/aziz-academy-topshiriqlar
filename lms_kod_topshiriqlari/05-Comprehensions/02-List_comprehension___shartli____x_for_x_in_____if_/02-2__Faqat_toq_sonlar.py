# INPUT: 1 qatorda butun sonlar
# VAZIFA: faqat toq sonlarni qoldiring
# OUTPUT: toq sonlar space bilan
# Agar bo‘sh bo‘lsa: BO'SH
a = map(int, input().split())
toq = [str(x) for x in a if x % 2 != 0]
if toq:
    print(" ".join(toq))
else:
    print("BO'SH")