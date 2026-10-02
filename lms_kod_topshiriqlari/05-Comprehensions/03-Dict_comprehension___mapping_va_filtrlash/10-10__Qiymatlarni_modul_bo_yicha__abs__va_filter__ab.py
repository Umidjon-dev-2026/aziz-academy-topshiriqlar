n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    abs_val = abs(int(value))
    if abs_val >= 5:
        d[key] = abs_val
print(d)