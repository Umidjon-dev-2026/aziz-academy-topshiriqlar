# INPUT: 1 qatorda butun sonlar
# VAZIFA: har bir son uchun:
#   x>0  -> 'pos'
#   x<0  -> 'neg'
#   x==0 -> 'zero'
# OUTPUT: label'lar space bilan
# Eslatma: if-else zanjiri list comprehension ichida
a = list(map(int, input().split()))
for x in a:
    if x > 0:
        print("pos", end=" ")
    elif x < 0:
        print("neg", end=" ")
    else:
        print("zero", end=" ")