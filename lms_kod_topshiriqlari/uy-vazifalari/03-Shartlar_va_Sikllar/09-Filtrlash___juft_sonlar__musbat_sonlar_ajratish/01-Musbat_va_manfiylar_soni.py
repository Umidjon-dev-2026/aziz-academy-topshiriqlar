n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
    
musbat = len([son for son in sonlar if son > 0])
manfiy = len([son for son in sonlar if son < 0])
print(musbat, manfiy)