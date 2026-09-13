# Kodingizni shu yerga yozing
n = int(input())
d = {}
for _ in range(n):
    kalit, son = input().split()
    d[kalit] = int(son)
print(min(d, key=d.get))