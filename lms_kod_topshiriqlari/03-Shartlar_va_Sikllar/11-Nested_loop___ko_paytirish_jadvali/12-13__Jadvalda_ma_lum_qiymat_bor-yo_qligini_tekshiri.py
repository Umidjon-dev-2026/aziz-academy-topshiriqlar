n, m = map(int, input().split())
x = int(input())
ok = False
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j == x:
            ok = True
print("Yes" if ok else "No")