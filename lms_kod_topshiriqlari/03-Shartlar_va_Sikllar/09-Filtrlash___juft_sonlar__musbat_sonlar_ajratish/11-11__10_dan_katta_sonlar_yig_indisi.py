n = int(input())
so = list(map(int, input().split()))
s = 0 
for x in so:
    if x > 10:
        s += x
print(s)