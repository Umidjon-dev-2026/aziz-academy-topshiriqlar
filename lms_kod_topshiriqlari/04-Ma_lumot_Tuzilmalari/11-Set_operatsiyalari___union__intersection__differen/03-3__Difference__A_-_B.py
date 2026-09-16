# 2 qator: A va B
# A - B ni toping.
# Agar bo‘sh bo‘lsa: BO'SH
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
a = a - b 
if a:
    print(*sorted(a))
else:
    print("BO'SH")