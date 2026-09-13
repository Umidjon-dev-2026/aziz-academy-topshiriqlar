# Kodingizni shu yerga yozing
s = input().strip()

hisob = {}

for harf in s:
    hisob[harf] = hisob.get(harf, 0) + 1
print(" ".join(f"{harf}:{soni}" for harf, soni in hisob.items()))