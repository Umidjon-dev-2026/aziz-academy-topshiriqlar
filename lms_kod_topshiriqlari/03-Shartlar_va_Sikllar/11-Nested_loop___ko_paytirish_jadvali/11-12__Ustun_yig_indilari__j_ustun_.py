n, m = map(int, input().split())
s = n * (n + 1) // 2 
for j in range(1, m + 1):
    print(j * s)