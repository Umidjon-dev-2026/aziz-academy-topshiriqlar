# Kodingizni shu yerga yozing
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = value
for k in sorted(d):
    print(k + "=" + d[k])