# n = int(input())
# d = {}
# for _ in range(n):
#     k, v = input().split()
#     d[k] = int(v)
# kalitlarni list qilib chiqaring
n = int(input())
d = {}
for i in range(n):
    k, v = input().split()
    d[k] = int(v)
print(list(d.keys()))