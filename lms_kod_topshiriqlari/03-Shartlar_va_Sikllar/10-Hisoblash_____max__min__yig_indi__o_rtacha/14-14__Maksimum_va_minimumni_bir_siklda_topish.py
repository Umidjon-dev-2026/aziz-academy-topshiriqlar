n = int(input())
a = list(map(int, input().split()))
mn = mx = a[0]
for x in a:
    if x < mn:
        mn = x
    if x > mx:
        mx = x
print(mx, mn)