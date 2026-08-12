n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
    
musbat_sonlar_yigindisi = sum([son for son in sonlar if son > 0])
print(musbat_sonlar_yigindisi)