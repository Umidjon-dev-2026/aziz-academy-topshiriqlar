n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    val_num = int(value)
    d[key] = 'even' if val_num % 2 == 0 else 'odd'
print(d)