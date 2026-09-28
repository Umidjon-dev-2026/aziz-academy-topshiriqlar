# Kodingizni shu yerga yozing
n = int(input())
jami = 0
for _ in range(n):
    narx = int(input())
    son = int(input())
    mahsulot = {'narx': narx, 'son': son}
    jami += mahsulot['narx'] * mahsulot['son']
print(jami)