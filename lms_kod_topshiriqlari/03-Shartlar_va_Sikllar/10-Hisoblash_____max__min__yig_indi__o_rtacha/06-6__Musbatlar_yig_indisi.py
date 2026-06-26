n= int(input())
nums = list(map(int, input().split()))
total = 0
for x in nums:
    if x > 0:
        total += x
print(total)