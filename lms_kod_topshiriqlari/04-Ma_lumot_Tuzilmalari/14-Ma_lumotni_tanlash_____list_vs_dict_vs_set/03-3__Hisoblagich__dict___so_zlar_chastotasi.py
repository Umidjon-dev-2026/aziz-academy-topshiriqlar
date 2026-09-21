# INPUT: 1 qatorda so‘zlar (space bilan)
# VAZIFA:
# - har bir so‘z (lower qilib) necha marta uchrashini dict orqali sanang
# OUTPUT:
# - har bir unikal so‘zni alifbo bo‘yicha sorted qilib chiqaring
# - format: word count
# Har biri yangi qatorda
a = input().split()
counts = {}
for word in a:
    w = word.lower()
    counts[w] = counts.get(w, 0) + 1
for word in sorted(counts.keys()):
    print(f"{word} {counts[word]}")