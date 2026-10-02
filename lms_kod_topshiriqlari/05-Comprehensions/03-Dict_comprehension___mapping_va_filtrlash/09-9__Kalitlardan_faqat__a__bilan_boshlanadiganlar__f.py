n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    if key.startswith('a'):
        d[key] = int(value)
print(d)