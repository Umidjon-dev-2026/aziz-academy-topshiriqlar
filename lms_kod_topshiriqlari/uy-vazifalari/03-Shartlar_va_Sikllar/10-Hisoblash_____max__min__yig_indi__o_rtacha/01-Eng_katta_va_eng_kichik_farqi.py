n = int(input())
sonlar = []
for i in range(n):
    son = int(input())
    sonlar.append(son)
    
farq = max(sonlar) - min(sonlar)

print(farq)