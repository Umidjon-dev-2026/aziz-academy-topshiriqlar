n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
    
sonlar.sort()
if n % 2 == 0:
    ortacha = (sonlar[n//2 - 1] + sonlar[n//2]) // 2
else:
    ortacha = sonlar[n // 2]

print(ortacha)