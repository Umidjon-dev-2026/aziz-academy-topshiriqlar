# INPUT:
# n
# n qator: key value
# VAZIFA: faqat value > 10 bo‘lgan juftliklarni qoldiring
# OUTPUT: yangi dict
n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    val_num = int(value)
    if val_num > 10:
        d[key] = val_num
print(d)