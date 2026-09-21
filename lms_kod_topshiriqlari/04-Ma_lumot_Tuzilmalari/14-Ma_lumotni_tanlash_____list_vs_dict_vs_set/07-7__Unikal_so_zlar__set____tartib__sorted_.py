# INPUT: 1 qatorda so‘zlar
# VAZIFA:
# - so‘zlarni lower qilib setga o‘tkazing (unikal)
# - sorted qilib chiqarish
# OUTPUT: unikal so‘zlar alifbo bo‘yicha
words = input().lower().split()
a = sorted(set(words))
print(*a)