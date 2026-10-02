# INPUT:
# n
# n qator: key value
# VAZIFA: yangi dict: value'lar 2 ga ko‘paytirilgan bo‘lsin
# OUTPUT: dict
n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value) * 2
print(d)