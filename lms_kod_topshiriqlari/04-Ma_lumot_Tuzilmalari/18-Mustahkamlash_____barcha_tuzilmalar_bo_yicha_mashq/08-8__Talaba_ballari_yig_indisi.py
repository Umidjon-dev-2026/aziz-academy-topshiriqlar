# Kodingizni shu yerga yozing
ism = input().strip()
ballar = list(map(int, input().split()))
d = {ism: ballar}
print(sum(d[ism]))