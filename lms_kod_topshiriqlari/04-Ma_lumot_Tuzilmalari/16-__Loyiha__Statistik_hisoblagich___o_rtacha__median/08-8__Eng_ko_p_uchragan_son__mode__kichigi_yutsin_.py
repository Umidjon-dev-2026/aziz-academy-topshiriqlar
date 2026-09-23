a = list(map(int, input().split()))
best_num = a[0]
max_count = 0
for num in sorted(set(a)):
    count = a.count(num)
    if count > max_count:
        max_count = count
        best_num = num
print(best_num)