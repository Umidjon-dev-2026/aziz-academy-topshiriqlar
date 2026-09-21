# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - har bir so‘z uzunligini setga o‘tkazing
# OUTPUT: unikal uzunliklarni sorted qilib space bilan chiqaring
words = input().split()
a = {len(word) for word in words}
print(*sorted(a))