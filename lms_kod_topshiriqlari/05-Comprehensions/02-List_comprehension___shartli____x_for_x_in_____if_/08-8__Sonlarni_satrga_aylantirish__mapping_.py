# INPUT: 1 qatorda butun sonlar
# VAZIFA: har bir sonni string ko‘rinishga aylantiring
# OUTPUT: natijalar space bilan (stringlar)
# Eslatma: mapping (list comprehension)
a = input().split()
b = [str(x) for x in a]
print(" ".join(b))