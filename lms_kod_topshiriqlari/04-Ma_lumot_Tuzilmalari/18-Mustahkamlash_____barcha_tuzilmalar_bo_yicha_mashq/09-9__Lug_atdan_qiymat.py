# Kodingizni shu yerga yozing
n = int(input())
d = {}
for _ in range(n):
    key, value = input().split()
    d[key] = value
target = input().strip()
print(d[target])