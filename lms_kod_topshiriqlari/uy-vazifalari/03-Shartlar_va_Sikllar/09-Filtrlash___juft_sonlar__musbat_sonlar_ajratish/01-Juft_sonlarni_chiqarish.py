n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)

juft_sonlar = [son for son in sonlar if son % 2 == 0]

for son in juft_sonlar:
    print(son)