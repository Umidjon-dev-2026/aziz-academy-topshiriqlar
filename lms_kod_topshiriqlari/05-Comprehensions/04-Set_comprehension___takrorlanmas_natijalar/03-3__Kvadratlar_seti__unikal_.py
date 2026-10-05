nums = list(map(int, input().split()))
squared = sorted({x ** 2 for x in nums})
print(*squared)