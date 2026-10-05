a = input().split()
x = sorted({a.lower() for a in a })
print(*x)