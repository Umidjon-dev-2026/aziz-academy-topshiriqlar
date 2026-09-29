# INPUT: 1 qatorda butun sonlar (space bilan)
# VAZIFA: faqat juft sonlarni qoldiring (filtering)
# OUTPUT: juft sonlar space bilan
# Agar juft son bo‘lmasa: BO'SH
# Eslatma: list comprehension + if (oxirida)
a = list(map(int, input().split()))
x = [str(x) for x in a if x % 2 == 0]
if x:
    print(" ".join(x))
else:
    print("BO'SH")