n = int(input())
sonlar = [int(input()) for _ in range(n)]

musbat_sonlar = [son for son in sonlar if son > 0]

if musbat_sonlar:
    ortacha = sum(musbat_sonlar) // len(musbat_sonlar)
    print(ortacha)
else:
    print(0)