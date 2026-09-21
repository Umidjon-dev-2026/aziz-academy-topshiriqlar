# Kodingizni shu yerga yozing
nums = input().split()
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1
res = sum(1 for count in counts.values() if count > 1)
print(res)