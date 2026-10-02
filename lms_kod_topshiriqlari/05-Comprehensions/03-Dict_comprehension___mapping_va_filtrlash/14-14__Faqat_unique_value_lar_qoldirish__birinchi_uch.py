n = int(input())
res = {}
seen_val = set()
for _ in range(n):
    key, value = input().split()
    value = int(value)
    if value not in seen_val:
        res[key] = value
        seen_val.add(value)
print(res)