n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
    
eng_katta_son = max(sonlar)
orni = sonlar.index(eng_katta_son) + 1

print(orni)