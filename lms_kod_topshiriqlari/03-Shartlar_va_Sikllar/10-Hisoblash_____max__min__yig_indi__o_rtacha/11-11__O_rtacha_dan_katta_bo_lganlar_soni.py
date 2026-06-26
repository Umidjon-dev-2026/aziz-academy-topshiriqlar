n = int(input())
a = list(map(int, input().split()))
avg = sum(a) / n
print(sum(1 for x in a if x > avg))