nums = list(map(int, input().split()))
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
a = [num for num, count in counts.items() if count == 1]
if a:
    print(*sorted(a))
else:
    print("EMPTY")