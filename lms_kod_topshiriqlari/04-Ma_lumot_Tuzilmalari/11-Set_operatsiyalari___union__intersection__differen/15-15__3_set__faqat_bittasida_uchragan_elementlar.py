# 3 qator: A, B, C (int)
# Vazifa: faqat BITTA setda bor elementlarni chiqaring.
# Ya'ni: element A da bor, lekin B va C da yo‘q; yoki B da bor, lekin A va C da yo‘q; yoki C da bor, lekin A va B da yo‘q.
# Natija: SORT qilingan elementlar space bilan.
# Agar bo‘sh bo‘lsa: BO'SH

A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
# TODO
res = (A - (B | C)) | (B - (A | C)) | (C - (A | B))
if res:
    print(" ".join(str(x) for x in sorted(res)))
else:
    print("BO'SH")