# 2 qator: A va B
# A ^ B (faqat bittasida borlar) ni toping.
# Agar bo‘sh bo‘lsa: BO'SH
# Aks holda: SORT qilingan elementlar space bilan

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
res = a ^ b
if res:
    print(*(sorted(res)))
else:
    print("BO'SH")