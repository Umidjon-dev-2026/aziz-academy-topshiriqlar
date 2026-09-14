# Kodingizni shu yerga yozing
n = int(input())
d = {}
for _ in range(n):
    a, b = input().split()
    d[a] = int(b)
print(sum(d.values()))