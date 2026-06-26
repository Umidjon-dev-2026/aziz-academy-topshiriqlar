# n beriladi.
# 1..n oralig‘idagi toq sonlar yig‘indisini for bilan top.
n = int(input())
y = 0
for i in range(1, n + 1, 2):
    if i % 2 != 0:
        y += i 
print(y)