n = int(input())
a = list(map(int, input().split()))
k = int(input())
print(min(a, key=lambda x: (abs(x - k), x)))