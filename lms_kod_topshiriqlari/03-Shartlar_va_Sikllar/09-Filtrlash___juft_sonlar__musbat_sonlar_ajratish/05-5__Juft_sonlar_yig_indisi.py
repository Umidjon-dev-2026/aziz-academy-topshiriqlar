n = int(input())
son = list(map(int, input().split()))
yig = 0
for i in son:
    if i % 2 == 0:
        yig += i 
print(yig)