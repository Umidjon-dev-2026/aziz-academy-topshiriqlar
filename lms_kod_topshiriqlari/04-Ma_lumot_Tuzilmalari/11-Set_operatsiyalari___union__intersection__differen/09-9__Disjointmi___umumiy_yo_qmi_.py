# 2 qator: A va B
# Agar A va B disjoint bo‘lsa (A ∩ B = ∅) YES, aks holda NO.

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
if a.isdisjoint(b):
    print("YES")
else:
    print("NO")