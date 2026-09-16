# 2 qator: A va B
# B - A ni toping.
# Agar bo‘sh bo‘lsa: BO'SH
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
x = b - a
if x:
    print(*(sorted(x)))
else:
    print("BO'SH")