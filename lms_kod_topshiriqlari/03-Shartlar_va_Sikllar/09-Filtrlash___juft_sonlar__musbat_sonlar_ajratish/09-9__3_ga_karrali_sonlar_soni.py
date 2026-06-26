n = int(input())
so = list(map(int, input().split()))
count = 0
for x in so:
    if x % 3 == 0:
        count += 1
print(count)