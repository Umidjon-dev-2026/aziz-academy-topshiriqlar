# 2 qator: A va B
# Intersection (A ∩ B) ni toping.
# Agar kesishma bo‘sh bo‘lsa: BO'SH chiqaring
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
res = a & b
if res:
    print(*(sorted(res)))
else:
    print("BO'SH")