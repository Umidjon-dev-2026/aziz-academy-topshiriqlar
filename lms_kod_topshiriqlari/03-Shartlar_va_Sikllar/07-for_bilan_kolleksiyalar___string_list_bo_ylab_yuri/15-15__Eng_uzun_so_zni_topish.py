# Bitta satr matn beriladi.
# So‘zlarga bo‘ling: words = input().split()
# for bilan eng uzun so‘zni topib chiqaring.
# Agar bir nechta bo‘lsa, birinchisini chiqaring.
words = input().split()
mx = ""
for w in words:
    if len(w) > len(mx):
        mx = w 
print(mx)