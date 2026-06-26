n = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())
c = 0 
for x in s:
    if a <= x <= b:
        c +=1
print(c)