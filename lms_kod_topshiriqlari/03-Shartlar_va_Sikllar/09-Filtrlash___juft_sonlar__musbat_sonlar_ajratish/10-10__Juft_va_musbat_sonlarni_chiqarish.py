n = int(input())
so = list(map(int, input().split()))
for x in so:
    if x > 0 and x % 2 == 0:
        print(x)