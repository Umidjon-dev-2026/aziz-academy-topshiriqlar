n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    val_num = int(value)
    if val_num % 2 == 0:
        d[key] = val_num
print(d)