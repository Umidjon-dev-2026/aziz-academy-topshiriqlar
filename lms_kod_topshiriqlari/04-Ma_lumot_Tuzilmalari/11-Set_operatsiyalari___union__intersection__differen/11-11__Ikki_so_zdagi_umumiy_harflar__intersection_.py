# 2 qator: 2 ta string
# Umumiy harflarni toping (set intersection).
# Natija: harflarni SORT qilib bitta qatorda chiqaring.
# Agar bo‘sh bo‘lsa: BO'SH

a = input().strip()
b = input().strip()
# TODO
res = set(a) & set(b)
if res:
    print(*(sorted(res)), sep='')
else:
    print("BO'SH")