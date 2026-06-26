n = int(input())
a = list(map(int, input().split()))
best = a[0]
best_cnt = 0
for x in a:
    cnt = 0 
    for y in a:
        if y == x:
            cnt += 1
    if cnt > best_cnt or (cnt == best_cnt and x < best):
        best = x
        best_cnt = cnt
print(best)