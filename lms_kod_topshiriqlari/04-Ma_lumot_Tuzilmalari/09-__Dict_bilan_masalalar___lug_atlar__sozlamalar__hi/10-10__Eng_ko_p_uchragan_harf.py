# Kodingizni shu yerga yozing
soz = input()
d = {}
for harf in soz:
    d[harf] = d.get(harf, 0) + 1
    
print(max(d, key=d.get))