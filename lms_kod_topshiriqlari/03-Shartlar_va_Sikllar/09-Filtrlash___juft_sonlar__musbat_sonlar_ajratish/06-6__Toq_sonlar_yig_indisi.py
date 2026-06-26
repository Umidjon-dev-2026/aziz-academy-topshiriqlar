n = int(input())
sonlar = list(map(int, input().split()))
s = 0 
for i in sonlar:
    if i % 2 == 1:
        s += i 
print(s)