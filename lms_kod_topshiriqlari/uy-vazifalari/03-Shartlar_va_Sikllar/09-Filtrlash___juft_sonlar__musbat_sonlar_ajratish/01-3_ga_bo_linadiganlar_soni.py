n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
a = len([son for son in sonlar if son % 3 == 0])
print(a)