n = int(input())
m = n // 2
for i in range(n):
    for j in range(n):
        if i == m or j == m:
            print('*', end='')
        else:
            print('.', end='')
    print()