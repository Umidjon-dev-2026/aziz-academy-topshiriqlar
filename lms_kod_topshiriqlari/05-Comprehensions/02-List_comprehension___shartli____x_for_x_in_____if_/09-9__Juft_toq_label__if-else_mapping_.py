# INPUT: 1 qatorda butun sonlar
# VAZIFA: har bir son uchun:
#   juft bo‘lsa -> 'even'
#   toq bo‘lsa  -> 'odd'
# OUTPUT: label'lar space bilan
# Eslatma: if-else mapping list comprehension ichida
a = list(map(int, input().split()))
for i in a:
    if i % 2 == 0:
        print("even", end=" ")
    else:
        print("odd", end=" ")