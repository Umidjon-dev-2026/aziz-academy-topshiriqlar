# n va keyin n ta son beriladi (hammasi bitta qatorda bo‘lishi mumkin).
# for bilan yig‘indini topib chiqar.
# Masalan input: 5\n1 2 3 4 5
n = int(input())
sonl = list(map(int, input().split()))
yigindi = 0 
for son in sonl:
    yigindi += son
print(yigindi)