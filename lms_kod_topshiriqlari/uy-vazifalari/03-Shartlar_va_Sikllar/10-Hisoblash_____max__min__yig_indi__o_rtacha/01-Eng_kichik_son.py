n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
    
eng_kichik_son = min(sonlar)

print(eng_kichik_son)