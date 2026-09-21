# INPUT:
# 1-qator: A sonlari
# 2-qator: B sonlari
# VAZIFA:
# - barcha (a,b) juftliklarni setga oling (unikal)
# OUTPUT:
# 1) avval juftliklar soni
# 2) keyin juftliklarni 'a b' ko‘rinishida sorted qilib har qatorda chiqaring
# Sorting: avval a, keyin b
A = list(map(int, input().split()))
B = list(map(int, input().split()))
pairs = set()
for a in A:
    for b in B:
        pairs.add((a, b))
sorted_pairs = sorted(pairs)
print(len(sorted_pairs))
for a, b in sorted_pairs:
    print(a, b)