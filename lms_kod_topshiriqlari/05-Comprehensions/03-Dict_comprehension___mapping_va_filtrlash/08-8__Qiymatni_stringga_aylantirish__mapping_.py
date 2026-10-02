n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = str(value)
print(d)