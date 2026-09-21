# INPUT: 1 qatorda butun sonlar
# VAZIFA:
# - unikal qiling (set)
# - kamayish bo‘yicha sort qiling
# - top-3 ni oling (agar kam bo‘lsa borini)
# OUTPUT: sonlarni space bilan chiqarish (desc)
nums = (list(map(int, input().split())))
a = sorted(set(nums), reverse=True)
top3 = a[:3]
print(*top3)