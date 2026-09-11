# n = int(input())
# d = {}
# for _ in range(n):
#     k, v = input().split()
#     d[k] = int(v)
# qiymatlarni chiqaring
n = int(input())
d = {}
for a in range(n):
    k, v = input().split()
    d[k] = int(v)
for i in d.values():
    print(i)