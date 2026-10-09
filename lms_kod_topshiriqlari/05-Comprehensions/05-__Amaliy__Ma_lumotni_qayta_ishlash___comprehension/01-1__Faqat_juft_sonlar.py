a = list(map(int, input().split()))
filtr = [x for x in a if x % 2 == 0]
print(filtr)