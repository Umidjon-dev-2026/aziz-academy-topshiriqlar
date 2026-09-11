n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)
a = {}
for k, v in d.items():
    a[k] = v * 2
print(a)