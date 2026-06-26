n = int(input())
a = list(map(int, input().split()))
s = 0 
count = 0
for x in a:
    s += x
    count += 1
print(s / count)