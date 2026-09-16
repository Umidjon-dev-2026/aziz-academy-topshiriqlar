# 2 qator: A va B
# Agar A ⊆ B bo‘lsa YES, aks holda NO chiqaring.

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
if a.issubset(b):
    print("YES")
else:
    print("NO")