n = int(input())
items = [input().split() for _ in range(n)]
x = int(input())
d = {k: int(v) for k, v in items if int(v) >= x}
print(d)