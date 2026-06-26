# n va n ta son beriladi, keyin x beriladi.
# for i in range(len(lst)) orqali yurib,
# x ga teng bo‘lgan birinchi element indexini chiqaring.
# Topilmasa -1 chiqaring.
n = int(input())
lst = list(map(int, input().split()))
x = int(input())
for i in range(n):
    if lst[i] == x:
        print(i)
        break
else:
    print(-1)