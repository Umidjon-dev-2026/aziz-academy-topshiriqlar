a = sorted(list(map(int, input().split())))
n = len(a)
if n % 2 == 1:
    median = a[n // 2]
else:
    median = (a[n // 2 - 1] + a[n // 2]) / 2
print(f"{median:.2f}")