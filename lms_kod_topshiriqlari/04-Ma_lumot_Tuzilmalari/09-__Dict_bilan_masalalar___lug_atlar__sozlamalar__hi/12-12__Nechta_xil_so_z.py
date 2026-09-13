# Kodingizni shu yerga yozing
n = int(input())
sozlar = {}
for _ in range(n):
    soz = input()
    sozlar[soz] = sozlar.get(soz, 0) + 1
    
print(len(sozlar))